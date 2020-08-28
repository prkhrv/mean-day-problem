""" 
Mean days

Problem: You are given a list with dates find thee mean day of the given list

Explanation: Given that the range of day values are 1-7 while Monday = 1 and Sunday = 7 
Find the "Meanest Day" of the list .

"Meanest Day" is the sum of values of all the days divided by total number of days

For Example:- Consider a list with dates ['04041996','09091999','26091996']
Meanest Day == Thursday

Explanation:-
Day on '04041996 is Thursday(4),
Day on '09091999' is Thursday(4),
Day on '26091996' is Thursday(4),

hence Meanest day = 4+4+4 // 3 ---> 4 (Thursday)

Input:- A list with dates in string format. ie. '01011997'

Output:- Name of the Mean Day
"""

import calendar
import datetime

date_list = ['04041996','09091999','26091996']


def mean_day(date_list):
    value_sum = 0
    for date in date_list:
        day_value = datetime.datetime.strptime(date, '%d%m%Y').weekday()+1 
        value_sum = value_sum + day_value
    mean_day = value_sum // len(date_list)
    return calendar.day_name[mean_day-1]


print(mean_day(date_list))