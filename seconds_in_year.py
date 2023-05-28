def seconds_in_year(leap):
  if leap:
    sec_in_year = 60 * 60 *24 * 366
    return f'\nSeconds in Leap year = {sec_in_year:,}\nbye!'
  else:
    sec_in_year = 60 * 60 *24 * 365
    return f'\nSeconds in Normal year = {sec_in_year:,}\nbye!'
    
    
numeric = False
while not numeric:
  year = input("How many seconds in:\n 1) Normal year\n 2) Leap year\n (Select the option number) ")
  if year.isnumeric() and int(year)==1:
    numeric = True
    print(seconds_in_year(False))
  elif year.isnumeric() and int(year)==2:
    numeric = True
    print(seconds_in_year(True))
  else:
    print("You should enter a valid number (1 or 2)\n")

