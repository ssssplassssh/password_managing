import tkinter as tk
from tkinter import ttk
from functional import receive

root3 = tk.Tk()

# To set the exact dimensions of a Tkinter window, you can use the geometry() method to set the dimensions in the format widthxheight+x+y, where width and height are the desired window dimensions, and x and y are the window's position on the screen.
root3.geometry("345x120+100+100")

frm3 = ttk.Frame(root3, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm3.grid()

# Additionally, you can use the resizable() method to set whether the window can be resized by the user.
root3.resizable(width=False, height=False)

header_data_box = ttk.Label(frm3, text='Receive Data')
header_data_box.grid(column=4, row=1)

data_label = ttk.Label(frm3, text='Input name of service: ')
data_label.grid(column=3, row=2)

data_entry = ttk.Entry(frm3)
data_entry.grid(column=4, row=2)


receive_btn = ttk.Button(frm3, text='Receive', command= lambda: receive())
receive_btn.grid(column=4, row=3)

exit_btn = ttk.Button(frm3, text='Exit', command=root3.destroy)
exit_btn.grid(column=4, row=4)

def data_field_processing(name_entry):
    service = name_entry.get()
    print('Input : ' + service)
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "Новий текст")
    return service


root3.mainloop()
