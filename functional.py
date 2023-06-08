import tkinter as tk
from tkinter import ttk
# Імпортуємо модуль tkinter для доступу до символу tk.END

# Створюємо функцію send_button_clicked, яка виконується при натисканні кнопки "Send"
def send_button_clicked(entry_text, frm, frk):
    text = entry_text.get()
    print('Input Text: ' + text)

    entry_text.delete(0, tk.END)
    
    entry_text.insert(0, "Новий текст")
    
    save_button = ttk.Button(frk, text='Save password to file', command=lambda: save_password_to_file(text))
    save_button.grid(column=0, row=0)
    save_button = ttk.Button(frk, text='Save password to file')
    save_button.grid(column=0, row=0)

def save_password_to_file(password):
    filename = 'passwords.txt'
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print('Password saved to file:', password)
