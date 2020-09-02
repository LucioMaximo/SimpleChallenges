# Create a function that takes a list with temperature type, temperature, and a second temperature type.
# The temperature types can be Celsius, Fahrenheit, or Kelvin. Return the temperature type (in the list)
# converted into the second temperature type.
# converter(["fahrenheit", 3] , "kelvin") ➞ 257.0
# Difficulty Very Hard


def tempconversion(starttemptype, desttemptype, temp):
    temp = int(temp)
    tempdict = {('celsius', 'fahrenheit'): temp * 9/5 + 32,
                ('celsius', 'kelvin'): temp + 273.15,
                ('kelvin', 'celsius'): temp - 273.15,
                ('kelvin', 'fahrenheit'): temp * 9 / 5 - 459.67,
                ('fahrenheit', 'celsius'): (temp - 32) * 5/9,
                ('fahrenheit', 'kelvin'): (temp + 459.67) * 5/9}

    return round(tempdict[(starttemptype, desttemptype)], 1)

tempmsg = input("Please enter STARTINGTEMPTYPE VALUE DESIREDTEMPTYPE: ")
templist = tempmsg.split(" ")
print(tempconversion(templist[0],templist[2],templist[1]))