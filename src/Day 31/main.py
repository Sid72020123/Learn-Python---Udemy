from random import choice
from tkinter import *
from tkinter import font
import pandas as pd

# ---------------------------- CONFIG ------------------------------- #

TIMER = 3000  # 3 seconds
FRONT_LANGUAGE = "Hindi"
BACK_LANGUAGE = "English"
try:
    WORDS = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    WORDS = pd.read_csv("data/hindi_words.csv").to_dict(orient="records")
# print(WORDS)

# ---------------------------- FUNCTIONS ------------------------------- #


def user_tick():
    WORDS.remove(random_word_info)
    pd.DataFrame(WORDS).to_csv("data/words_to_learn.csv", index=False)
    show_random_word()


def show_random_word():
    global flip_timer
    global random_word_info
    window.after_cancel(flip_timer)

    random_word_info = choice(WORDS)
    word = random_word_info["Word"]
    transliteration = random_word_info["Transliteration"]
    translated = random_word_info["Translated"]

    canvas.itemconfig(canvas_image, image=front_card_image)
    canvas.itemconfig(
        title_text, text=FRONT_LANGUAGE, fill="black", font=hindi_word_font
    )
    canvas.itemconfig(word_text, text=word, fill="black")
    canvas.itemconfig(transliteration_text, text=transliteration)

    flip_timer = window.after(TIMER, lambda: show_translation(translated))


def show_translation(translated):
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(title_text, text=BACK_LANGUAGE, fill="white")
    canvas.itemconfig(word_text, text=translated, fill="white", font=word_font)
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
hindi_word_font = font.Font(family="Noto Sans Devanagari", size=60, weight="bold")

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
    image=tick_button_image, highlightthickness=0, command=user_tick
)

wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

flip_timer = window.after(0, lambda: ...)
show_random_word()

window.mainloop()
