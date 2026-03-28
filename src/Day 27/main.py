import tkinter

window = tkinter.Tk()

window.title("GUI Window")
window.minsize(width=500, height=300)

# Add padding
window.config(padx=20, pady=20)  # This method can also be used on individual components

# Label
label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
# label.pack()
# label.place(x=0, y=0)
label.grid(column=0, row=0)


# Button
def button_clicked():
    print("Button was clicked!")
    print(input_text.get())
    # label.config(text="The button was clicked!")


button = tkinter.Button(text="This is a button!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = tkinter.Button(text="This is another button!", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input_text = tkinter.Entry(width=10)
input_text.insert(tkinter.END, string="Some text to begin with.")
print(input_text.get())
# input_text.pack()
input_text.grid(column=3, row=2)

window.mainloop()

"""
# Text
text = tkinter.Text(height=5, width=30)
text.focus()

text.insert(tkinter.END, "Example of multi-line text entry.")
print(
    text.get("1.0", tkinter.END)
)  # Get the current value in textbox at line 1, character 0
text.pack()


# Spinbox 
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.pack()


# Radio
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = tkinter.Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Banana", "Orange", "Pear"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
"""


"""
# *args: Many Positional Arguments


def add(*args):
    print(sum(args))


add(10, 20, 30)


# *kwargs: Many keyword Arguments


def add(**kwargs):
    for keyword, value in kwargs.items():
        print(keyword, "->", value)
    print(sum(kwargs.values()))


add(a=10, b=20, c=30)
"""
