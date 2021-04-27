import time
import re


def get_noun():
    while True:
        noun = input("Enter a noun: ")
        if len(noun) == 0:
            continue
        return noun


def get_verb():
    while True:
        verb = input("Enter a verb: ")
        if len(verb) == 0:
            continue
        return verb


def get_adjective():
    while True:
        adjective = input("Enter a adjective: ")
        if len(adjective) == 0:
            continue
        return adjective


def get_maddies(words):
    maddies = {}

    for each in words:
        if re.match(r"^noun", each):
            maddies[each] = get_noun()
        if re.match(r"^verb", each):
            maddies[each] = get_verb()
        if re.match(r"^adj", each):
            maddies[each] = get_adjective()

    return maddies


with open("story.txt") as file:
    story = file.read()

sub = re.findall(r"\{(\w+\d+)\}", story) # return a list of all the matches
madlibs = get_maddies(set(sub))

for each in sub:
    story = story.replace("{" + each + "}", madlibs[each])


print("Creating the story....")
time.sleep(2)
print(story)


