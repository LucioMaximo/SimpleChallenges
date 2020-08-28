# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# format_date("11/12/2019") ➞ "20191211"
# difficulty: Medium
def dateformat(date):
    sdate = date.split("/")
    return print(sdate[2]+sdate[1]+sdate[0])


dateformat("11/12/2019")
