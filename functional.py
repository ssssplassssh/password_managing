# Імпортуємо модуль tkinter для доступу до символу tk.END
import tkinter as tk
import json

# Реалізація функції обробки поля з введеним значенням, отримання значення і виведення в консоль, очищення всього поля і заміна на нове значення "Новий текст"

def field_processing(name_entry):
    field_value = name_entry.get()
    print('Input : ' + field_value)
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "Новий текст")
    return field_value

# Створюємо функцію save_button_clicked, яка виконується при натисканні кнопки "Save"

def save_button_clicked(service_entry, login_entry, email_entry, password_entry):
    
    # Виклик функцій для обробки поля
    
    service = field_processing(service_entry)  
    login = field_processing(login_entry)  
    email = field_processing(email_entry)
    password = field_processing(password_entry)
    
    # Словник для зберігання у форматі .json 
    data = {
        "Service": service,
        "Login": login,
        "Email": email,
        "Password": password
    }
    
    # Зберігання у файл .json 
    
    save_data_to_file(data)
    
    # Зберігання у файл .txt
    
    # save_data_to_file(service, login, email, password)
    
# Зберігання у файл .json 

def save_data_to_file(data):
    filename = 'info.json' # file name
    try: # перехоплює помилки при зберіганні
        with open(filename, 'r') as file: # спроба прочитати файл
            saved_data = json.load(file) # якщо файл існує і містить дійсний об'єкт, то він буде завантажений через json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): # якщо файл не існує або містить недійсний json виникає помилка і файл набуває пустого списку
        saved_data = []
    
    saved_data.append(data) # додавання даних у файл
     
    with open(filename, 'w') as file: # відкриття файлу для запису
        json.dump(saved_data, file, indent=4) # зберігання у форматі json і встановлення відступів
    
    print(f"Data saved to file:\n{data}")
        

# Зберігання у файл .txt

# def save_data_to_file(service, login, email, password):
#     filename = 'info.txt'
#     with open(filename, 'a') as file:
#         file.write(service + '\n')
#         file.write(login + '\n')
#         file.write(email + '\n')
#         file.write(password + '\n')
#     print(f" Data saved to file: \n Service:  {service} \n Login:  {login} \n Email: {email} \n Password:  {password} \n")
            
            
            