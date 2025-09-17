items = ['soap', 'toothpaste', 'shampoo', 'deodorant', 'towel', 'plate', 'fork', 'sponge', 'detergent', 'paper']
prices = [50,40,70,60,150,100,30,20,120,8]
amount = []
cart = []
total = 0

print('''* Soap $50
* Toothpaste $40
* Shampoo $70
* Deodorant $60
* Towel $150
* Plate $100
* Fork $30
* Sponge $20
* Detergent $120
* Paper $8''')

print('Add items to cart(use q for quiting):')

count = 0
while True:
    item = input(f'item {count + 1}:')
    cart.append(item)
    if item == 'q':
        break
    else:
        idx = items.index(item)
        amount.append(prices[idx])
    count +=1

print(f'{'='*30}')
count = 0
for item in cart:
    if item == 'q':
        break
    else:
        print(f'{item} : ${amount[count]}')
        total = total + amount[count]
        count +=1
print()

print('-- These are items in cart! --')
print(f'{'='*30}')

print(f'TOTAL : ${total}')

