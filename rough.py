year = 2025
data = (year % 4 == 0 and year % 100 != 0) or (year % 400)

if data :
    print ('29')
else:
    print('28')

month_names = ['Jan','Fed','Mar','Apr']