# --- OOP in Python ---

# Class & Objects


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.is_active = True
        self.followers = 0
        self.following = 0

    def print_user_info(self):
        display_fields = {
            "Name": self.name,
            "Age": self.age,
            "Followers": self.followers,
            "Following": self.following,
        }
        display_text = "\n\t".join(
            [f"{field}: {value}" for field, value in display_fields.items()]
        )
        print(f"User {self.name}:\n\t{display_text}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("A", 0)
user_1.print_user_info()

user_2 = User("B", 1)
user_2.print_user_info()

user_1.follow(user_2)
user_2.follow(user_1)

print("*" * 30)

user_1.print_user_info()
user_2.print_user_info()
# print(isinstance(user_1, User))
