# Create a function that takes two numbers as arguments and return their sum.
# addition(3, 2) ➞ 5

def addition (a,b): return print("addition("+a+", "+b+") ➞ "+str(int(a)+int(b)))

Addition = input("Please Enter the two numbers you wish to add, separated by a space. E.g:1 2  :")
[a,b] = Addition.split(" ")
addition(a,b)