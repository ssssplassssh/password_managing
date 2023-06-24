import tkinter as tk
from tkinter import ttk
import functional as fn

# Creating the main window

root = tk.Tk()

# We adjust the configuration of columns and rows for the main window
root.columnconfigure(0, minsize=250)
root.rowconfigure([0 ,1], minsize=250)

# Створюємо мітку для заголовка
header_box = tk.Label(text='Password Managing')
header_box.pack()

############################Frames#################################

# We create a "frm" frame for placing interface elements
frm = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm.pack()

# We create a "frk" frame for other interface elements
frk = ttk.Frame(root, padding=10, relief=tk.SUNKEN, borderwidth=5)
frk.pack()

############################# Buttons #############################

# We create an "Exit" button to close the program

exit_btn = ttk.Button(frm, text='Exit', command=root.destroy)
exit_btn.grid(column=4, row=11)

# So when the "Send" button is clicked, an anonymous function is executed, which then calls the functional.send_button_clicked function with the entry_text parameter.
# Using an anonymous function allows you to pass parameters to the functional.send_button_clicked function without having to use a named function. It is a convenient way to call a function with parameters when you need to pass additional arguments or variables to the event handler function
# Create a "Send" button to call the send_button_clicked function from the functional module, which processes the entered password

save_json_btn = ttk.Button(frm, text='Save in .json',command=lambda: fn.save_button_clicked_json(service_entry, login_entry, email_entry, password_entry))
save_json_btn.grid(column=4, row=9)

save_txt_btn = ttk.Button(frm, text='Save in .txt', command=lambda: fn.save_button_clicked_txt(service_entry, login_entry, email_entry, password_entry))
save_txt_btn.grid(column=4, row=10)

take_data_btn = ttk.Button(frm, text='Take data', command=lambda: fn.receive_data(), )
take_data_btn.grid(column=2, row=9)


info_btn = ttk.Button(frm, text='Info', command=lambda: fn.take_info())
info_btn.grid(column=2, row=10)

#############################Entries###############################

# We create an entry_text input field for entering login

service_entry = ttk.Entry(frm, foreground='black')
service_entry.grid(column=4, row=5)

login_entry = ttk.Entry(frm, foreground='green')
login_entry.grid(column=4, row=6)

# We create an email_entry input field for entering email

email_entry = ttk.Entry(frm, foreground='blue')
email_entry.grid(column=4, row=7)

# We create a password_entry input field for entering a password

password_entry = ttk.Entry(frm, foreground='red')
password_entry.grid(column=4, row=8)


#################################Labels############################

# We create a login_label label for signing the service input field

service_label = ttk.Label(frm, text='Input Service: ' )
service_label.grid(column=2, row=5)

# We create a login_label label for signing the login input field

login_label = ttk.Label(frm, text='Input Login: ' )
login_label.grid(column=2, row=6)

# We create a label email_label for the signature to the email input field

email_label = ttk.Label(frm, text='Input Email: ' )
email_label.grid(column=2, row=7)

# We create a password_label label for the signature to the password input field

password_label = ttk.Label(frm, text='Input Password: ')
password_label.grid(column=2, row=8)

# Running the Tkinter main loop
root.mainloop()
