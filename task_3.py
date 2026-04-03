import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

# Загружаем группы
if os.path.exists("save.json"):
    with open("save.json", "r") as f:
        gruppy = json.load(f)
else:
    gruppy = {}

# Получаем курсы
valuty = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["Valute"]

# Показать все валюты
def vse():
    listbox.delete(0, tk.END)
    for k in valuty:
        listbox.insert(tk.END, f"{k} - {valuty[k]['Name']}: {valuty[k]['Value']} руб.")

# Найти валюту
def nayti():
    kod = vvod.get().upper()
    if kod in valuty:
        messagebox.showinfo("Курс", f"{kod}: {valuty[kod]['Value']} руб.")
    else:
        messagebox.showerror("Ошибка", "Нет такой валюты")

# Сохранить группы
def save():
    with open("save.json", "w") as f:
        json.dump(gruppy, f, ensure_ascii=False)

# Показать группы
def pokazat_gruppy():
    listbox2.delete(0, tk.END)
    for n in gruppy:
        listbox2.insert(tk.END, f"{n}: {gruppy[n]}")

# Создать группу
def sozdat():
    name = entry.get()
    if name and name not in gruppy:
        gruppy[name] = []
        save()
        pokazat_gruppy()

# Добавить в группу
def dobavit():
    if not listbox2.curselection() or not listbox.curselection():
        return
    name = listbox2.get(listbox2.curselection()[0]).split(":")[0]
    kod = listbox.get(listbox.curselection()[0]).split(" - ")[0]
    if kod not in gruppy[name]:
        gruppy[name].append(kod)
        save()
        pokazat_gruppy()

# Удалить из группы
def udalit():
    if not listbox2.curselection():
        return
    name = listbox2.get(listbox2.curselection()[0]).split(":")[0]
    if not gruppy[name]:
        return
    kod = gruppy[name][0]
    gruppy[name].remove(kod)
    save()
    pokazat_gruppy()

# Окно
root = tk.Tk()
root.title("Курс валют")
root.geometry("500x600")

# Все валюты
tk.Label(root, text="ВСЕ ВАЛЮТЫ").pack()
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)
tk.Button(root, text="Обновить", command=vse).pack()

# Поиск
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Код:").pack(side=tk.LEFT)
vvod = tk.Entry(frame, width=10)
vvod.pack(side=tk.LEFT)
tk.Button(frame, text="Найти", command=nayti).pack(side=tk.LEFT)

# Мои группы
tk.Label(root, text="МОИ ГРУППЫ").pack(pady=(10,0))
listbox2 = tk.Listbox(root)
listbox2.pack(fill=tk.BOTH, expand=True)

# Управление группами
frame2 = tk.Frame(root)
frame2.pack(pady=5)
entry = tk.Entry(frame2, width=15)
entry.pack(side=tk.LEFT)
tk.Button(frame2, text="Создать", command=sozdat).pack(side=tk.LEFT)

tk.Button(root, text="Добавить в группу", command=dobavit).pack()
tk.Button(root, text="Удалить из группы", command=udalit).pack(pady=(0,10))

vse()
pokazat_gruppy()
root.mainloop()