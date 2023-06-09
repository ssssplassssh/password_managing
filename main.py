import tkinter as tk
from tkinter import ttk
import functional as fn

# Створення головного вікна
root = tk.Tk()

# Налаштовуємо конфігурацію колонок та рядків для головного вікна
root.columnconfigure(0, minsize=250)
root.rowconfigure([0 ,1], minsize=250)

# Створюємо мітку для заголовка
header_box = tk.Label(text='Password Managing')
header_box.pack()

############################Frames#################################

# Створюємо рамку frm для розміщення елементів інтерфейсу
frm = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm.pack()

# Створюємо рамку frk для інших елементів інтерфейсу
frk = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frk.pack()

############################# Buttons #############################

# Створюємо кнопку "Exit" для закриття програми

exit_btn = ttk.Button(frm, text='Exit', command=root.destroy)
exit_btn.grid(column=4, row=10)

# Таким чином, коли кнопка "Send" натискається, виконується анонімна функція, яка потім викликає функцію functional.send_button_clicked з параметром entry_text.
# Використання анонімної функції дозволяє передати параметри до функції functional.send_button_clicked без необхідності використання іменованої функції. Вона є зручним способом виклику функції з параметрами у випадку, коли потрібно передати додаткові аргументи або змінні до функції обробки події
# Створюємо кнопку "Send" для виклику функції send_button_clicked з модуля functional, яка обробляє введений пароль

send_btn = ttk.Button(frm, text='Save',command=lambda: fn.save_button_clicked(service_entry, login_entry, email_entry, password_entry))
send_btn.grid(column=4, row=9)



#############################Entries###############################

# Створюємо поле введення entry_text для введення login.

service_entry = ttk.Entry(frm, foreground='black')
service_entry.grid(column=4, row=5)

login_entry = ttk.Entry(frm, foreground='green')
login_entry.grid(column=4, row=6)

# Створюємо поле введення email_entry для введення email.

email_entry = ttk.Entry(frm, foreground='blue')
email_entry.grid(column=4, row=7)

# Створюємо поле введення password_entry для введення password.

password_entry = ttk.Entry(frm, foreground='red')
password_entry.grid(column=4, row=8)


#################################Labels############################

# Створюємо мітку login_label для підпису до поля введення service

service_label = ttk.Label(frm, text='Input Service: ' )
service_label.grid(column=2, row=5)

# Створюємо мітку login_label для підпису до поля введення login

login_label = ttk.Label(frm, text='Input Login: ' )
login_label.grid(column=2, row=6)

# Створюємо мітку email_label для підпису до поля введення email

email_label = ttk.Label(frm, text='Input Email: ' )
email_label.grid(column=2, row=7)

# Створюємо мітку password_label для підпису до поля введення password

password_label = ttk.Label(frm, text='Input Password: ')
password_label.grid(column=2, row=8)

# Запуск головного циклу Tkinter
root.mainloop()
