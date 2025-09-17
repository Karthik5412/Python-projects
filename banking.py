def showbalance(balance):
    print('='*35)
    print(f'Your Balance : ${balance:.2f}')
    print('='*35)

def withdraw(balance):
    amount = float(input('Enter amount to withdraw:'))
    if amount > balance:
        return 0
    elif amount < 0:
        print('Entre valid amount')
        return 0
    else:
        return amount

def deposite(balance):
    amount=float(input('Enter amount:'))
    if amount < 0:
        print('Enter Valid amount')
        return 0
    else:
        return amount
    

def main():
    inprocess = True
    accounts = {'1124': 1500, '2481':1000, '3391':1075, '1185':1150,'6382':1200}

    print('*'*35)
    print('WELCOME TO OUR BANK')
    print('*'*35)
    acc = input('Enter Account Number:')
    print()
    if acc in accounts.keys():
        print('In Progress')
        while inprocess:
            print('*'*35)
            print('1.Balance')
            print('2.With Draw')
            print('3.Deposite')
            print('4.Exit')
            print('*'*35)

            choice = int(input('Enter your choice:'))

            match choice:
                case 1:
                    showbalance(accounts.get(acc))
                case 2:
                    accounts[acc] -= withdraw(accounts.get(acc))

                case 3:
                    accounts[acc] += deposite(accounts.get(acc))
                case 4:
                    inprocess = False
                case _:
                    print('Invalid choice \n Make a valid one')
    else:
        print('Your not a member of our bank')

if __name__ == '__main__':
    main()


