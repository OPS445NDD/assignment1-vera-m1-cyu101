#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Jared Yu"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28

    mon_max = {
        1:31,
        2:feb_max,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    return mon_max[month]
def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return False

def valid_date(date: str) -> bool:
    "return True if date is valid YYYY-MM-DD format"

    if len(date) != 10:
        return False
    
    if date[4] != '-' or date[7] != '-':
        return False

    str_year, str_month, str_day = date.split('-')

    if not str_year.isdigit() or not str_month.isdigit() or not str_day.isdigit():
        return False

    year = int(str_year)
    month = int(str_month)
    day = int(str_day)


    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True
    
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "count Saturdays and Sundays between start_date and stop_date"

    count = 0
    current_date = start_date

    while current_date != after(stop_date):

        str_year, str_month, str_day = current_date.split('-')

        day = day_of_week(
            int(str_year),
            int(str_month),
            int(str_day)
        )

        if day == 'sat' or day == 'sun':
            count += 1

        current_date = after(current_date)

    return count
    ...

if __name__ == "__main__":
    ...
