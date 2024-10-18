#!/usr/bin/env python3

import calendar

print("WELCOME TO YOUR CALENDER CHECK, ENTER ANY YEAR BELOW")

tired = False
while not tired:
    get_year = int(input("Enter the year you want to check: "))
    mycal = calendar.TextCalendar()
    print(mycal.formatyear(get_year))
    cont = input("Do you still want to check another year?(yes or no):  ").lower()
    if cont == "no":
        print("Alright, have a great day. Bye!!!")
        tired = True
        break
