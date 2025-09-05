def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400)

def days_count(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if isleap(year) is True:
            return 29
        else:
            return 28
    
def first_day_of_month(month,year):
    if month < 3:
        month += 12
        year -= 1
    
    q = 1
    k = year % 100
    j = year//100
    h = (q + ((13*(month+1))//5) + k + (k//4) + j - 2*j) % 7
    return (h+5)%7

def the_calender(month,year):
    total_days = days_count(month,year)
    fday = first_day_of_month(month,year)
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']

    print(f'{' ' * 11}{year}')
    print(f'{' ' * ((27-len(month_names[month-1]))//2)}{month_names[month-1]}')
    

    print('SUN MON TUE WED THU FRI SAT')
    for _ in range(fday):
        print('   ', end =' ')
    
    for day in range(1,total_days+1):
        print(f'{day:3}', end =' ')

        if (fday + day) % 7 == 0:
            print('')
    print('')



year = int(input('Enter year:'))
print()
for month in range(1,13):
    the_calender(month,year)
    print()