import tkinter as tk
from tkinter import ttk
root4 = tk.Tk()

# To set the exact dimensions of a Tkinter window, you can use the geometry() method to set the dimensions in the format widthxheight+x+y, where width and height are the desired window dimensions, and x and y are the window's position on the screen.
root4.geometry("260x130+100+100")

frm4 = ttk.Frame(root4, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm4.grid()

# Additionally, you can use the resizable() method to set whether the window can be resized by the user.
root4.resizable(width=False, height=False)


# def data_field_processing(data_entry):
#     field_value = data_entry.get()
#     print('Input : ' + field_value)
#     name_entry.delete(0, tk.END)
#     name_entry.insert(0, "Новий текст")
#     return field_value


header_data_box = ttk.Label(frm4, text=f'Your Data on  service')
header_data_box.grid(column=4, row=1)

data_label = ttk.Label(frm4, text='Login: ')
data_label.grid(column=3, row=2)

data_label = ttk.Label(frm4, text='Email: ')
data_label.grid(column=3, row=3)

data_label = ttk.Label(frm4, text='Password: ')
data_label.grid(column=3, row=4)

data_entry = ttk.Entry(frm4)
data_entry.grid(column=4, row=2)

data_entry = ttk.Entry(frm4)
data_entry.grid(column=4, row=3)

data_entry = ttk.Entry(frm4)
data_entry.grid(column=4, row=4)


exit_btn = ttk.Button(frm4, text='Exit', command=root4.destroy)
exit_btn.grid(column=4, row=5)

root4.mainloop()
