# password_managing

sudo apt-get install python3-tk

Widgets Class:
Label, Button, Entry, Text, Frame

Classic(tkinet.Label) vs Themed Widgets(tkinter.ttk.Label)

Label:
text="Hello, Tkinter",
foreground="white",  # or fg. Set the text color to white 
background="black"  # or bg. Set the background color to black
width=10,
height=10

Отримання багаторядкового введення користувача за допомогою текстових віджетів:
>>> window = tk.Tk()
>>> text_box = tk.Text()
>>> text_box.pack()

Adjusting Frame Appearance With Reliefs
tk.FLAT: Has no border effect (the default value)
tk.SUNKEN: Creates a sunken effect
tk.RAISED: Creates a raised effect
tk.GROOVE: Creates a grooved border effect
tk.RIDGE: Creates a ridged effect

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

Widget Class	Variable Name Prefix	Example
Label	            lbl	                lbl_name
Button	            btn	                btn_submit
Entry	            ent	                ent_age
Text	            txt	                txt_notes
Frame	            frm	                frm_address

Controlling Layout With Geometry Managers:
.place()
.grid()

frame1.pack(fill=tk.Y, side=tk.LEFT):
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
tk.TOP
tk.BOTTOM
tk.LEFT
tk.RIGHT

The .place() Geometry Manager:
label2.place(x=75, y=75)

The .grid() Geometry Manager:
frame.grid(row=i, column=j)

.grid()	.pack()
sticky="ns"	fill=tk.Y
sticky="ew"	fill=tk.X
sticky="nsew"	fill=tk.BOTH