# program to check age in python
from datetime import datetime

Current_year=int(datetime.now().strftime('%Y'))   #taking current year

Birth_year=int(input('Enter your Birth Year : '))

print(f'You are {Current_year-Birth_year} years old ')
