# In this challenge, sort a list containing a series of dates given as strings. Each date is given in the format
# DD-MM-YYYY_HH:MM: "12-02-2012_13:44" The priority of criteria used for sorting will be:
#
#     Year
#     Month
#     Day
#     Hours
#     Minutes
#
# Given a list lst and a string mode, implement a function that returns:
#
#     if mode is equal to "ASC", the list lst sorted in ascending order.
#     if mode is equal to "DSC", the list lst sorted in descending order.
#    Remember: the date is in the format DD-MM-YYYY_HH:MM.
# You can expect only valid formatted dates, without exceptions to handle.
# sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC")
#          ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]
# Difficulty: Very Hard     (added my own CSV file to read for added complexity)
import csv
from datetime import datetime

with open('Files/Dates2.csv', newline='', encoding='utf-8-sig') as f:

    reader = csv.reader(f, delimiter=',')
    datelist = []
    acdc = 0
    for row in reader:
        datelist.append(row[0])
        if row[1] == "ASC" or row[1] == "DSC":
            acdc = row[1]


def date_sort(ascdsc):
    datelist.sort(key=lambda x: datetime.strptime(x, '%d-%m-%Y_%H:%M'))
    return datelist if ascdsc == "ASC" else datelist[::-1]


print(date_sort(acdc))
