import tkinter as tk
from tkinter import messagebox
import requests

def get_user():
    username = entry_username.get()  # берём username из поля ввода
    if not username:
        messagebox.showwarning("Ошибка", "Введите username")
        return

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Ошибка", "Пользователь не найден")
        return

    data = response.json()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Имя: {data['login']}\n")
    result_text.insert(tk.END, f"Ссылка: {data['html_url']}\n")
    result_text.insert(tk.END, f"Репозитории: {data['public_repos']}\n")
    result_text.insert(tk.END, f"Подписчики: {data['followers']}\n")
    result_text.insert(tk.END, f"Подписки: {data['following']}\n")

root = tk.Tk()
root.title("GitHub Viewer")
root.geometry("400x300")

label_username = tk.Label(root, text="Введите username GitHub:")
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

button_get = tk.Button(root, text="Получить профиль", command=get_user)
button_get.pack(pady=5)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

root.mainloop()