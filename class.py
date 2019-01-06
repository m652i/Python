def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print('leap year')
        return True
    elif year % 400 == 0:
        print('400 leap year')
        return True
    else:
        print('not leap')
        return False
    
year = int(input('Please enter the year: '))
if len(str(year)) != 4:
    print('Enter a 4 digit year')
else:
    yrResult = leap(year)
    print(yrResult)
