# Temparature convertor

temp = float(input('Enter temparature : '))
init_temp = input('Enter units of temp : ')
final_temp = input('Enter units of convert temp : ')

if init_temp.strip().lower() in ['celcius','c'] :
    if final_temp.strip().lower() in ['fahrenheit','f'] :
        print(f'{((9/5)*temp)+32} ^F')
    elif final_temp.strip().lower() in ['kelvin','k'] :
        print(f'{temp + 273.15} K')
    elif final_temp.strip().lower() in ['rankine','r'] :
        print(f'{((9/5)*temp)+491.67} ^R')

elif init_temp.strip().lower() in ['fahrenheit','f'] :
    if final_temp.strip().lower() in ['celcius','c'] :
        print(f'{((5/9)*temp)-32} ^C')
    elif final_temp.strip().lower() in ['kelvin','k'] :
        print(f'{(5/9)*(temp-32) + 273.15} K')
    elif final_temp.strip().lower() in ['rankine','r'] :
        print(f'{temp+459.67} ^R')


elif init_temp.strip().lower() in ['kelvin','k'] :
    if final_temp.strip().lower() in ['fahrenheit','f'] :
        print(f'{((9/5)*(temp-273.15))+32} ^F')
    elif final_temp.strip().lower() in ['celcius','c'] :
        print(f'{273.15 - temp} ^ C')
    elif final_temp.strip().lower() in ['rankine','r'] :
        print(f'{((9/5)*temp)} ^R')

elif init_temp.strip().lower() in ['rankine','r'] :
    if final_temp.strip().lower() in ['fahrenheit','f'] :
        print(f'{temp-459.67} ^F')
    elif final_temp.strip().lower() in ['celcius','c'] :
        print(f'{(5/9)* (temp - 491.67)} ^ C')
    elif final_temp.strip().lower() in ['kelvin','k'] :
        print(f'{(5/9) * temp} K')

else :
    li = ['celcius','c','fahrenheit','f','kelvin','k','rankine','r']
    
    if init_temp not in li and final_temp not in li  :
        print(f'{init_temp} and {final_temp} both are invalid')
    
    elif init_temp not in li :
        print(f'{init_temp} is invalid')

    elif final_temp not in li :
        print(f'{final_temp} is invalid')


    


    