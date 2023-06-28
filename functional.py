# Import the tkinter module to access the tk.END symbol
import subprocess
import tkinter as tk
import json

# Implementation of the function of processing the field with the entered value, obtaining the value and outputting it to the console, clearing the entire field and replacing it with a new value "New text"

def field_processing(name_entry):
    field_value = name_entry.get()
    print('Input : ' + field_value)
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "Новий текст")
    return field_value

# We create the save_button_clicked function, which is executed when the "Save" button is pressed

def save_button_clicked_json(service_entry, login_entry, email_entry, password_entry):
    
    # Call functions to process the field
    service = field_processing(service_entry)  
    login = field_processing(login_entry)  
    email = field_processing(email_entry)
    password = field_processing(password_entry)
    
    # Dictionary to store in the format .json 
    data = {
        "Service": service,
        "Login": login,
        "Email": email,
        "Password": password
    }
    
    # Save in file .json 
    if data["Service"] == '' and data["Login"] == '' and data["Email"] == '' and data["Password"] == '':
        pass
    else:
       save_data_to_file_json(data)
            
def save_button_clicked_txt(service_entry, login_entry, email_entry, password_entry):
 
    # Call functions to process the field
    service = field_processing(service_entry)  
    login = field_processing(login_entry)  
    email = field_processing(email_entry)
    password = field_processing(password_entry)
    
    if service == '' and login == '' and email == '' and password== '':
        pass
    else:
        save_data_to_file_txt(service, login, email, password)
    
# Save in file .json 

def save_data_to_file_json(data):
    filename = 'info.json' # file name
    try: # intercepts storage errors
        with open(filename, 'r') as file: # trying to read a file
            saved_data = json.load(file) # if the file exists and contains a valid object, it will be loaded via json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): # if the file does not exist or contains invalid json, an error occurs and the file becomes an empty list
        saved_data = []
    
    saved_data.append(data) # adding data to a file
     
    with open(filename, 'w') as file: # opening a file for writing
        json.dump(saved_data, file, indent=4) # saving in json format and setting indents
    
    print(f"Data saved to file:\n{data}")

# Save in file .txt

def save_data_to_file_txt(service, login, email, password):
    filename = 'info.txt'
    with open(filename, 'a') as file:
        file.write(service + '\n')
        file.write(login + '\n')
        file.write(email + '\n')
        file.write(password + '\n')
    print(f" Data saved to file: \n Service:  {service} \n Login:  {login} \n Email: {email} \n Password:  {password} \n")

def take_info():
    subprocess.Popen(["python3", "info_window.py"])

# from data_window import get_data_entry

def receive_data():
    # data_entry = get_data_entry()
    # filename = 'info.json'
    # service_name = field_processing(data_entry)

    # with open(filename, 'r') as file:
    #     saved_data = json.load(file)

    # for data in saved_data:
    #     if data["Service"] == service_name:
    #         print("Знайдено відповідні дані:")
    #         print(f"Service: {data['Service']}")
    #         print(f"Login: {data['Login']}")
    #         print(f"Email: {data['Email']}")
    #         print(f"Password: {data['Password']}")
    #         break
    # else:
    #     print("Дані не знайдено")
    subprocess.Popen(["python3", "data_window.py"])

        
def receive():
    subprocess.Popen(["python3", "receive_data_window.py"])
    
