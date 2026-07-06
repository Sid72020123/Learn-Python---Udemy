from random import choice
from tkinter import *
import pandas as pd

# ---------------------------- CONFIG ------------------------------- #

TIMER = 3000  # 3 seconds
FRONT_LANGUAGE = "Hindi"
BACK_LANGUAGE = "English"
WORDS = pd.read_csv("data/hindi_words.csv").to_dict(orient="records")
# print(WORDS)

# ---------------------------- FUNCTIONS ------------------------------- #


def show_random_word():
    random_word_info = choice(WORDS)
    word = random_word_info["Word"]
    transliteration = random_word_info["Transliteration"]
    translated = random_word_info["Translated"]

    canvas.itemconfig(canvas_image, image=front_card_image)
    canvas.itemconfig(title_text, text=FRONT_LANGUAGE)
    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(transliteration_text, text=transliteration)

    window.after(TIMER, lambda: show_translation(translated))


def show_translation(translated):
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(title_text, text=BACK_LANGUAGE)
    canvas.itemconfig(word_text, text=translated)
    canvas.itemconfig(transliteration_text, text="")


# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
language_font = ("Ariel", 35, "italic")
word_font = ("Ariel", 60, "bold")
transliteration_font = ("Ariel", 15, "italic")

window = Tk()
window.title("Lang Flashy")
# window.geometry("885x700")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
cross_button_image = PhotoImage(file="images/wrong.png")
tick_button_image = PhotoImage(file="images/right.png")

canvas_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="title", font=language_font)
word_text = canvas.create_text(400, 263, text="word", font=word_font)
transliteration_text = canvas.create_text(
    400, 400, text="(transliteration)", font=transliteration_font, fill="gray"
)

wrong_button = Button(
    image=cross_button_image, highlightthickness=0, command=show_random_word
)
correct_button = Button(
    image=tick_button_image, highlightthickness=0, command=show_random_word
)

wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

window.mainloop()
