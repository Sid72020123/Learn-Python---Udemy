from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import pathlib
from tkinter import *
from random import choice

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

PASSWORD_LENGTH = 8


def generate_random_password():
    characters = ascii_uppercase + ascii_lowercase + digits + punctuation
    result = "".join(choice(characters) for _ in range(PASSWORD_LENGTH))
    password_input.delete(0, END)
    password_input.insert(0, result)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password(website, username, password):
    path = pathlib.Path("passwords.txt")
    if not path.exists():
        f = open("passwords.txt", "w")
        titles = ["Website", "Username / Email", "Password"]
        for title in titles:
            f.write(f"| {title.center(50)} |")
        f.write("\n")
        f.close()
    with open("passwords.txt", "a+") as file:
        file.write(
            f"| {website.center(50)} || {username.center(50)} || {password.center(50)} |\n"
        )


def add_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    save_password(website, username, password)
    website_input.delete(0, END)
    password_input.delete(0, END)


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
generate_button = Button(text="Generate Password", command=generate_random_password)
add_button = Button(text="Add", width=36, command=add_password)

website_input.focus()
username_input.insert(0, "common_email@abc.xyz")
website_input.grid(row=1, column=1, columnspan=2)
username_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
