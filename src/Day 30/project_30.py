# --- Project 30 ---

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from json import load, dump, decoder
import json
import pathlib
from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

PASSWORD_LENGTH = 8


def generate_random_password():
    characters = ascii_uppercase + ascii_lowercase + digits + punctuation
    result = "".join(choice(characters) for _ in range(PASSWORD_LENGTH))
    password_input.delete(0, END)
    password_input.insert(0, result)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password(website, username, password):
    data = {website: {"username": username, "password": password}}

    path = pathlib.Path("passwords.json")
    if not path.exists():
        f = open("passwords.json", "x")
        f.close()
    with open("passwords.json", "r") as file:
        try:
            passwords = load(file)
        except decoder.JSONDecodeError:
            passwords = {}
    with open("passwords.json", "w") as file:
        passwords.update(data)
        dump(passwords, file, indent=4)


def add_password():
    website = str(website_input.get()).strip()
    username = username_input.get()
    password = password_input.get()

    if not (website and username and password):
        messagebox.showerror(
            title="Fields Empty!",
            message="Some fields are empty!\nPlease fill all the required fields...",
        )
        return

    confirm_save = messagebox.askokcancel(
        title="Confirm Entry",
        message=f"These are the details entered:\nWebsite: {website}\nUsername / Email: {username}\nPassword: {password}\n\nSave the entry?",
    )

    if confirm_save:
        save_password(website, username, password)
        pyperclip.copy(password)
        website_input.delete(0, END)
        password_input.delete(0, END)


def search_password():
    website = str(website_input.get()).strip()

    if not website:
        messagebox.showerror(
            title="Field Empty!",
            message="Website field is empty!",
        )
        return

    with open("passwords.json", "r") as file:
        passwords = load(file)
        if website in passwords:
            website_info = passwords[website]
            messagebox.showinfo(
                title="Website entry found!",
                message=f"Entry found!\n\nWebsite: {website}\n\nUsername: {website_info['username']}\nPassword: {website_info['password']}",
            )
        else:
            messagebox.showwarning(
                title="Website entry not found!",
                message="The website entry was not found!",
            )


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

website_input = Entry(width=22)
username_input = Entry(width=40)
password_input = Entry(width=21)
search_button = Button(text="Search", command=search_password)
generate_button = Button(text="Generate Password", command=generate_random_password)
add_button = Button(text="Add", width=36, command=add_password)

website_input.focus()
username_input.insert(0, "common_email@abc.xyz")
website_input.grid(row=1, column=1)
username_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
search_button.grid(row=1, column=2)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
