import random


class Game:
    def __init__(self, max_attempts=3):
        self.number = random.randint(1, 10)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.won = False

    def guess(self, number):
        self.attempts += 1

        if number == self.number:
            print("Congrats, you won!")
            self.won = True
        elif number < self.number:
            print("Guess again but higher..")
        else:
            print("Guess again but lower...")

        if self.attempts == self.max_attempts and not self.won:
            print(f"You lose! The number to guess was {self.number}")


game = Game()

print("Welcome to my game - Guess the Number")

while not game.won and game.attempts < game.max_attempts:
    num = int(input("Guess the number ( 1 to 10): "))
    game.guess(num)


