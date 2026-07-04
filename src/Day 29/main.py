from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

BG = "white"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

canvas = Canvas(height=200, width=200, bg=BG, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=BG)
username_label = Label(text="Email/Username:", bg=BG)
password_label = Label(text="Password:", bg=BG)

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
username_input = Entry(width=35)
password_input = Entry(width=21)
generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36)

website_input.grid(row=1, column=1, columnspan=2)
username_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
