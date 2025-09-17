menu = {"zinger": 150,
"spicy burger": 160,
"pizza": 180,
"margherita pizza": 150,
"parcel": 85,
"momos": 110,
"fries": 140,
"peri fries": 150,
"frankie": 120,
"sandwich": 150,
"burger": 90,
"fried rice": 170,
"hakka noodles": 160,
"chilli paneer": 220,
"wrap": 90,
"tikka": 250,
"garlic bread": 120,
"shake": 180,
"coffee": 130,
"masala fries": 110
}

print(f'{'-'*10} Todays\'s Menu {'-'*10}')
for key, value in menu.items():
    print(f'{key:18} : ${value:.2f}')

print(f'{'-'*35}')

cart =[]
total = 0

print()
print('Enter item to buy:(e for exit):')
while True:
    food = input('- ').lower()
    if food == 'e':
        break
    elif food in menu.keys():
        cart.append(food)
        total += menu.get(food)
    else :
        print(f'{food} is not available')

print()

print(f'{'-'*11} YOUR ITEMS {'-'*11}')
for item in cart:
    print(f'{item.upper():15} : ${menu.get(item):.2f}')
print(f'{'-'*35}')

print(f'YOU WANT TO PAY : ${total:.2f}/- only')

