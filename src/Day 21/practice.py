# Class Inheritance in Python


class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale.")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


fish = Fish()
fish.breathe()
fish.swim()
