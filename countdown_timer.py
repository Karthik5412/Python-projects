import time

my_time = int(input('Enter time:'))

for x in range(my_time, 0,-1) :
    sec = x % 60
    min = int(x/60)%60
    print(f'00:{min:02}:{sec:02}')
    time.sleep(1)

print(f"Time\'s up !")
