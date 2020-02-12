# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n_m = input()
n, m = n_m.split()

special = '.|.'
counter = 1

for x in range(int(n)):
    if x == math.floor(float(n)/2):
        for w in range(math.floor(float(m)/2) - 3):
            print('-', end='')
        print('WELCOME', end='')
        for w in range(math.floor(float(m)/2) + 4, int(m)):
            print('-', end='')
    else:
        if x <= math.floor(float(n)/2):
            for y in range(math.floor(float(m)/2) - math.floor(counter*1.5)):
                print('-', end='')
            for y in range(counter):
                print(special, end='')
            for y in range(math.floor(float(m)/2) + math.floor(counter*1.5) + 1, int(m)):
                print('-', end='')
            counter += 2            
        else:
            counter -= 2   
            for y in range(math.floor(float(m)/2) - math.floor(counter*1.5)):
                print('-', end='')
            for y in range(counter):
                print(special, end='')
            for y in range(math.floor(float(m)/2) + math.floor(counter*1.5) + 1, int(m)):
                print('-', end='')
    print('')
