# --- Project 24 ---

with open("starting_letter.txt", "r") as file:
    LETTER_TEMPLATE = file.read()

with open("invited_names.txt", "r") as file:
    invited_names = file.readlines()

invited_names = list(map(lambda x: x.strip(), invited_names))

for name in invited_names:
    with open(f"./letters-output/{name}.txt", "w") as file:
        file.write(LETTER_TEMPLATE.replace("[name]", name))
