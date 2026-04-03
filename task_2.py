import psutil
import tkinter as tk

root = tk.Tk()
root.title("Монитор системы")
root.geometry("400x200")  # уменьшил размер, так как текста немного

text_output = tk.Text(root, height=10, width=40)
text_output.pack(pady=10)


def stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    text_output.delete(1.0, tk.END)

    text_output.insert(tk.END, f"CPU: {cpu_usage}%\n")
    text_output.insert(tk.END, f"RAM: {memory_usage}%\n")
    text_output.insert(tk.END, f"Disk: {disk_usage}%\n")

    root.after(2000, stats)

stats()
root.mainloop()