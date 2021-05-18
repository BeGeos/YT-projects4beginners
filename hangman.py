import re
import random


class Letter:

    def __init__(self, letter):
        self.letter = letter
        if re.match(r"[a-zA-Z]", letter):
            self.display = False
            self.default = "_ "
        else:
            self.display = True


with open("words.txt") as file:
    text = file.read()

# first Method
# words_list = re.split(r"\n", text)
# secret_word = random.choice(words_list)

# second method
start = round(random.random() * len(text))
end = start + 50
secret_word = re.split(r"\n", text[start: end])[1]


def hangman(word):

    checklist = [i.lower() for i in word if re.match(r"[a-zA-Z]", i)]
    display_list = [Letter(i) for i in word]

    score = 10

    while score > 0:
        guess_word = ""

        for letter in display_list:
            if letter.display:
                guess_word += letter.letter
            else:
                guess_word += letter.default

        print(f"Your score is {score}")
        print(guess_word)

        if len(checklist) == 0:
            print(f"You won, and the score is {score}")

        guess_letter = input("Enter a letter: ")
        if guess_letter.lower() in checklist:
            checklist = [i.lower() for i in checklist if i != guess_letter.lower()]

            for j in display_list:
                if j.letter.lower() == guess_letter.lower():
                    j.display = True
        else:
            score -= 1

    print(f"Sorry you lost the guy is dead. The word is {word}")


if __name__ == "__main__":
    while True:
        hangman(secret_word)
        play_again = input("Do you want to play again? Y/Any key\n")
        if play_again.lower() == "y":
            continue
        else:
            print("Ok, bye bye")
            quit()


