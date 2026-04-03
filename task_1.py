import tkinter as tk
import requests


def check():
    listbox.delete(0, tk.END)

    urls = [
        "https://github.com/",
        "https://www.binance.com/en",
        "https://tomtit.tomsk.ru/",
        "https://jsonplaceholder.typicode.com/",
        "https://moodle.tomtit-tomsk.ru/",
        "https://metanit.com/python/tkinter/2.1.php"
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            code = response.status_code

            if 200 <= code < 300:
                status = "ДОСТУПЕН"
            elif code == 403:
                status = "ВХОД ЗАПРЕЩЕН"
            elif code == 404:
                status = "НЕ НАЙДЕН"
            elif code >= 500:
                status = "ОШИБКА СЕРВЕРА"
            else:
                status = "НЕ ДОСТУПЕН"
        except:
            status = "НЕ ДОСТУПЕН"
            code = "ОШИБКА"

        listbox.insert(tk.END, f"{url} → {status} → {code}")


window = tk.Tk()
window.title("Проверка сайтов")
window.geometry("800x300")

label = tk.Label(window, text="Нажми кнопку для проверки сайтов", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(window, text="ПРОВЕРИТЬ", command=check, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

listbox = tk.Listbox(window, font=("Arial", 10), height=10)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

window.mainloop()