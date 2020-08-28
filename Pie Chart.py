# A pie chart is a circular graphical representation of a dataset, where each category frequency is represented by
# a slice (or circular sector) with an amplitude in degrees given by the single frequency percentage over the total of
# frequencies. You can obtain the degrees of sectors following these steps:

# Calculate frequencies total.
# Calculate percentage of every category frequency dividing it by the frequencies total.
# Transform every percentage in degrees multiplying it for 360.

# You are given a dictionary data with keys being the data categories (represented by letters) and values being the data
# frequencies. Implement a function that returns a map to design a pie chart, like to say the same dictionary with
# values transformed in degrees instead of frequencies. Round final values to the nearest tenth.
# pie_chart({ "a": 30, "b": 15, "c": 55 }) ➞ { "a": 108, "b": 54, "c": 198 }
# difficulty Very Hard

import matplotlib.pyplot as plt


def pie_chart(labels, sizes):

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()


SegNumber = int(input("Welcome to the bakery. Please enter the total size of your data set: "))
x = 0
label = []
numbers = []
while SegNumber >= 1:

        Data = input("Please enter data entry "+str(x+1)+". Use the format NAME NUMBER: ")
        sdata = Data.split(" ")
        label.append(sdata[0])
        numbers.append(sdata[1])
        x += 1
        SegNumber -= 1

pie_chart(label, numbers)
