# Create a function that takes a string txt and censors any word from a given list lst.
# The text removed must be replaced by the given character char.
# e.g censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
# difficulty: Hard

censoredwords = ["Today", "a", "cow", "over", "did", "chicken", "road"]


def censorer(sentence):
    censoredsentence = ""
    words = sentence.split(" ")
    for x in words:
        if x.lower() in (y.lower() for y in censoredwords):
            censoredsentence += " " + "*"*len(x)
        else:
            censoredsentence += " " + x

    return print(censoredsentence)


Input = input("Please speak your mind:")
censorer(Input)
