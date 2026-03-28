# --- Project 27 ---

import tkinter

window = tkinter.Tk()
window.title("mile to km converter")
# window.minsize(width=500, height=300)

window.config(padx=20, pady=20)

LABELS = {"miles": [2, 0], "is equal to": [0, 1], "km": [2, 1]}

number_input = tkinter.Entry(width=10)
number_input.insert(tkinter.END, string="0")
number_input.grid(column=1, row=0)

for label, positions in LABELS.items():
    l = tkinter.Label(text=label)
    l.grid(column=positions[0], row=positions[1])


def calculate():
    miles = float(number_input.get())
    kilometers = miles * 1.609344
    answer_label.config(text=f"{kilometers:.2f}")


answer_label = tkinter.Label(text="0")
answer_label.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
