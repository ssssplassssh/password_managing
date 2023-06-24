import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root2 = tk.Tk()

# To set the exact dimensions of a Tkinter window, you can use the geometry() method to set the dimensions in the format widthxheight+x+y, where width and height are the desired window dimensions, and x and y are the window's position on the screen.
root2.geometry("360x260+100+100")

frm2 = ttk.Frame(root2, padding=10, relief=tk.SUNKEN, borderwidth=5)
frm2.grid()

# Additionally, you can use the resizable() method to set whether the window can be resized by the user.
root2.resizable(width=False, height=False)

header_info_box = ttk.Label(frm2, text='Info about this program')
header_info_box.grid(column=6, row=1)

# Creating a scrolledtext.Text object
text_info = scrolledtext.ScrolledText(frm2, width=40, height=10)
text_info.grid(column=6, row=2)

# Setting the text in the Text widget
text_info.insert(tk.END, "This program allows you to create and save data, namely a login, email, and password for a certain resource, site, or service. The information is recorded in a JSON format file. So later, data output will be available using a query.")

# Disabling the editing of the text
text_info.configure(state="disabled")

exit_btn = ttk.Button(frm2, text='Exit', command=root2.destroy)
exit_btn.grid(column=6, row=9)

root2.mainloop()
