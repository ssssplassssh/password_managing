import tkinter as tk
from tkinter import ttk
import functional as fn

# Creating the main window
root = tk.Tk()

# We adjust the configuration of columns and rows for the main window
root.columnconfigure(0, minsize=250)
root.rowconfigure([0, 1], minsize=250)

# Creating a header label
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

# Create a "Save in .json" button to call the save_button_clicked_json function
save_json_btn = ttk.Button(frm, text='Save in .json', command=lambda: fn.save_button_clicked_json(service_entry, login_entry, email_entry, password_entry))
save_json_btn.grid(column=4, row=9)

# Create a "Save in .txt" button to call the save_button_clicked_txt function
save_txt_btn = ttk.Button(frm, text='Save in .txt', command=lambda: fn.save_button_clicked_txt(service_entry, login_entry, email_entry, password_entry))
save_txt_btn.grid(column=4, row=10)


# Create a "Take data" button to call the receive_data function
take_data_btn = ttk.Button(frm, text='Take data', command= lambda: fn.receive_data())
take_data_btn.grid(column=2, row=9)

# Create an "Info" button to call the take_info function
info_btn = ttk.Button(frm, text='Info', command = lambda: fn.take_info)
info_btn.grid(column=2, row=10)

#############################Entries###############################

# We create an entry_text input field for entering the service name
service_entry = ttk.Entry(frm, foreground='black')
service_entry.grid(column=4, row=5)

# We create an entry_text input field for entering the login
login_entry = ttk.Entry(frm, foreground='green')
login_entry.grid(column=4, row=6)

# We create an entry_text input field for entering the email
email_entry = ttk.Entry(frm, foreground='blue')
email_entry.grid(column=4, row=7)

# We create an entry_text input field for entering the password
password_entry = ttk.Entry(frm, foreground='red')
password_entry.grid(column=4, row=8)

#################################Labels############################

# We create a label for the service input field
service_label = ttk.Label(frm, text='Input Service:')
service_label.grid(column=2, row=5)

# We create a label for the login input field
login_label = ttk.Label(frm, text='Input Login:')
login_label.grid(column=2, row=6)

# We create a label for the email input field
email_label = ttk.Label(frm, text='Input Email:')
email_label.grid(column=2, row=7)

# We create a label for the password input field
password_label = ttk.Label(frm, text='Input Password:')
password_label.grid(column=2, row=8)

# Running the Tkinter main loop
root.mainloop()
