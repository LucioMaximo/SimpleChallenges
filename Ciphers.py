# It's time to send and receive secret messages.

# Create a single function that takes a string or a list and returns a coded or decoded message.

# The first letter of the string, or the first element of the list represents the Character Code of that letter.
# The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.
# Difficulty: Very Hard

def cipher(msg):

    if type(msg) == str:
        return [ord(msg[0])] + [ord(msg[a]) - ord(msg[a-1]) for a in range(1, len(msg))]
    print(msg)
    return ''.join(chr(sum((msg[:i]))) for i in range(1, len(msg) + 1))


message = input("Please enter your message captain: ")
print(cipher([110, -9, 0, -1, -68, 66, -1, 2, 8, 10, -5]))


