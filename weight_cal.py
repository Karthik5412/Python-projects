weight = input('Enter your weight along with units: ')

if 'kg' in weight :
    we = weight.replace('kg'or' kg','')
    w = int(we) * 2.205
    print(f'{w} lbs is your weight in pounds')

elif 'lbs' in weight :
    we = weight.replace('lbs'or' lbs','')
    w = int(we) / 2.205
    print(f'{round(w,3)} kg is your weight in kilograms')
else :
    print(f'{weight} is not allowed')

