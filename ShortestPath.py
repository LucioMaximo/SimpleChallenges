# Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits
# each city and returns to the origin city?
# Return the total number of possible paths a salesman can travel, given n paths.
# paths(4) ➞ 24
# Difficulty: Easy
import math
def shortestpath(n): return print("There are "+str(math.factorial(int(n)))+" possible paths between "+n+" cities")


Cities = input("Please enter the amount of cities:")
shortestpath(Cities)

