# --- Project 14 ---

# Higher or Lower Game

from os import system
from random import choice

LOGO = """    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \\/ _ \\/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\\__, /_/ /_/\\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \\ | /| / / _ \\/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\\____/|__/|__/\\___/_/     
"""

vs = """ 
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

GAME_DATA = data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman and Self-Made Billionaire",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 149,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Beyoncé",
        "follower_count": 145,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Neymar",
        "follower_count": 138,
        "description": "Footballer",
        "country": "Brasil",
    },
    {
        "name": "National Geographic",
        "follower_count": 135,
        "description": "Magazine",
        "country": "United States",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 133,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 131,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 127,
        "description": "Reality TV personality and Model",
        "country": "United States",
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 119,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 113,
        "description": "Musician",
        "country": "Trinidad and Tobago",
    },
    {
        "name": "Nike",
        "follower_count": 109,
        "description": "Sportswear multinational",
        "country": "United States",
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 108,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 107,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Katy Perry",
        "follower_count": 94,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Kourtney Kardashian",
        "follower_count": 90,
        "description": "Reality TV personality",
        "country": "United States",
    },
    {
        "name": "Kevin Hart",
        "follower_count": 89,
        "description": "Comedian and actor",
        "country": "United States",
    },
    {
        "name": "Ellen DeGeneres",
        "follower_count": 87,
        "description": "Comedian",
        "country": "United States",
    },
    {
        "name": "Real Madrid CF",
        "follower_count": 86,
        "description": "Football club",
        "country": "Spain",
    },
    {
        "name": "FC Barcelona",
        "follower_count": 85,
        "description": "Football club",
        "country": "Spain",
    },
    {
        "name": "Rihanna",
        "follower_count": 81,
        "description": "Musician and businesswoman",
        "country": "Barbados",
    },
    {
        "name": "Demi Lovato",
        "follower_count": 80,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Victoria's Secret",
        "follower_count": 69,
        "description": "Lingerie brand",
        "country": "United States",
    },
    {
        "name": "Zendaya",
        "follower_count": 68,
        "description": "Actress and musician",
        "country": "United States",
    },
    {
        "name": "Shakira",
        "follower_count": 66,
        "description": "Musician",
        "country": "Colombia",
    },
    {
        "name": "Drake",
        "follower_count": 65,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Chris Brown",
        "follower_count": 64,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "LeBron James",
        "follower_count": 63,
        "description": "Basketball player",
        "country": "United States",
    },
    {
        "name": "Vin Diesel",
        "follower_count": 62,
        "description": "Actor",
        "country": "United States",
    },
    {
        "name": "Cardi B",
        "follower_count": 67,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "David Beckham",
        "follower_count": 82,
        "description": "Footballer",
        "country": "United Kingdom",
    },
    {
        "name": "Billie Eilish",
        "follower_count": 61,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Justin Timberlake",
        "follower_count": 59,
        "description": "Musician and actor",
        "country": "United States",
    },
    {
        "name": "UEFA Champions League",
        "follower_count": 58,
        "description": "Club football competition",
        "country": "Europe",
    },
    {
        "name": "NASA",
        "follower_count": 56,
        "description": "Space agency",
        "country": "United States",
    },
    {
        "name": "Emma Watson",
        "follower_count": 56,
        "description": "Actress",
        "country": "United Kingdom",
    },
    {
        "name": "Shawn Mendes",
        "follower_count": 57,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 55,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Gigi Hadid",
        "follower_count": 54,
        "description": "Model",
        "country": "United States",
    },
    {
        "name": "Priyanka Chopra Jonas",
        "follower_count": 53,
        "description": "Actress and musician",
        "country": "India",
    },
    {
        "name": "9GAG",
        "follower_count": 52,
        "description": "Social media platform",
        "country": "China",
    },
    {
        "name": "Ronaldinho",
        "follower_count": 51,
        "description": "Footballer",
        "country": "Brasil",
    },
    {
        "name": "Maluma",
        "follower_count": 50,
        "description": "Musician",
        "country": "Colombia",
    },
    {
        "name": "Camila Cabello",
        "follower_count": 49,
        "description": "Musician",
        "country": "Cuba",
    },
    {
        "name": "NBA",
        "follower_count": 47,
        "description": "Club Basketball Competition",
        "country": "United States",
    },
]

print(LOGO)


def clear_screen():
    system("clear")


def get_random_profile():
    profile_data = choice(GAME_DATA)

    return (
        profile_data["follower_count"],
        f"{profile_data['name']}, a {profile_data['description']}, from {profile_data['country']}.",
    )


score = 0
is_game_over = False
profile_1_followers, description_1 = get_random_profile()

while not is_game_over:
    clear_screen()
    print(LOGO)

    if score > 0:
        print(f"That's correct! Your current score is {score}.\n")

    profile_2_followers, description_2 = get_random_profile()
    if profile_1_followers == profile_2_followers:
        profile_2_followers, description_2 = get_random_profile()
    profile_followers = [profile_1_followers, profile_2_followers]
    descriptions = [description_1, description_2]
    # print(profile_followers) # --> Cheat :P

    print("Compare A:", description_1, end="")
    print(vs)
    print("Compare B:", description_2)

    user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

    allowed_choices = {"a": 0, "b": 1}
    if user_choice not in allowed_choices.keys():
        print("Invalid Choice Entered. Game Over!")
        print("Final Score:", score)
        is_game_over = True
    else:
        current_chosen_item = profile_followers.pop(allowed_choices[user_choice])
        current_chosen_item_description = descriptions.pop(allowed_choices[user_choice])
        other_item = profile_followers[0]

        if current_chosen_item > other_item:
            score += 1
            profile_1_followers, description_1 = (
                current_chosen_item,
                current_chosen_item_description,
            )
        else:
            clear_screen()
            print(LOGO)
            print(f"\nThat's incorrect, your final score is {score}.")
            is_game_over = True
