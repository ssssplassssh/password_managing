import tkinter as tk
from tkinter import ttk
import functional as fn
'''
# Створення головного вікна
root = tk.Tk()
text_box = tk.Text()
label_box = tk.Label(text='HEADER')
label_box.pack()
text_box.pack()

# Створення рамок для елементів інтерфейсу
frm = ttk.Frame(root, padding=10)
frm.pack() # встановлюємо їх позицію у головному вікні 

frs = ttk.Frame(root, padding=40)
frs.pack() # встановлюємо їх позицію у головному вікні 

# Створення мітки
ttk.Label(frs, text="Це мітка", width=20).grid(column=1, row=2) # grid - розміщення в сітці

entry = ttk.Entry(frs, text='It`s Entry', width=50)
entry.grid(column=1, row=4)

ttk.Button(frs, text="Send").grid(column=1, row=5)

# Функція, яка викликається при натисканні кнопки "Send"
def send_button_clicked():
    # Отримати введений текст
    text = entry.get()
    print("Введений текст:", text)
    
    # Очистити поле введення,  видаляє весь текст з початку до кінця поля введення (включаючи обидва кінці)
    entry.delete(0, tk.END)

    # Вставити новий текст в поле введення
    entry.insert(0, "Новий текст")

# Прив'язка функції до кнопки "Send"
ttk.Button(frs, text="Send", command=send_button_clicked).grid(column=1, row=5)

# Створення кнопки
ttk.Button(frs, text="Це кнопка").grid(column=1, row=3)

# Створення мітки та кнопки в рамці
ttk.Label(frm, text="Hello World!", foreground='white', background='black').grid(column=0, row=0)

ttk.Button(frm, text="Quit",width=20,command=root.destroy).grid(column=1, row=0) # command=root.destroy - команда що закриває вікно
'''

# Створення головного вікна
root = tk.Tk()

# Налаштовуємо конфігурацію колонок та рядків для головного вікна
root.columnconfigure(0, minsize=250)
root.rowconfigure([0 ,1], minsize=250)

# Створюємо мітку для заголовка
header_box = tk.Label(text='Password Managing')
header_box.pack()

# Створюємо рамку frm для розміщення елементів інтерфейсу
frm = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm.pack()

# Створюємо рамку frk для інших елементів інтерфейсу
frk = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frk.pack()

# Створюємо кнопку "Exit" для закриття програми
exit_btn = ttk.Button(frm, text='Exit', command=root.destroy)
exit_btn.grid(column=4, row=10)

# Створюємо поле введення entry_text для введення пароля.
entry_text = ttk.Entry(frm, foreground='red')
entry_text.grid(column=4, row=8)

# Таким чином, коли кнопка "Send" натискається, виконується анонімна функція, яка потім викликає функцію functional.send_button_clicked з параметром entry_text.
# Використання анонімної функції дозволяє передати параметри до функції functional.send_button_clicked без необхідності використання іменованої функції. Вона є зручним способом виклику функції з параметрами у випадку, коли потрібно передати додаткові аргументи або змінні до функції обробки події
# Створюємо кнопку "Send" для виклику функції send_button_clicked з модуля functional, яка обробляє введений пароль
send_btn = ttk.Button(frm, text='Send',command=lambda: fn.send_button_clicked(entry_text, frm, frk))
send_btn.grid(column=4, row=9)

# Створюємо мітку entry_text_label для підпису до поля введення пароля
entry_text_label = ttk.Label(frm, text='Input Password: ')
entry_text_label.grid(column=2, row=8)


# Запуск головного циклу Tkinter
root.mainloop()
