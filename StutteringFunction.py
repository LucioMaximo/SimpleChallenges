# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice
# with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
# stutter("incredible") ➞ "in... in... incredible?"

def stutter(word):
    stutteredword = (word[:2]+"... ")*2+word+"?"
    return print("stutter("+word+") ➞ "+stutteredword)


w = input("What did you say?: ")
stutter(w)
