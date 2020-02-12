def print_rangoli(size):
    first = 'a'
    last = chr(ord(first) + size - 1)
    for x in range(2*size-2 + 1):
        for y in range(2*size-2 - 2*x):
            print('-', end='')
        for y in range(2*size-2 - 2*x, 0):
            print('-', end='')
        if (2*size-2 - 2*x) >= 0:
            for l in range(ord(last), ord(first) + size - 2 - x, -1):
                if (size == 1):
                    print(chr(l) + '', end='')        
                else:
                    print(chr(l) + '-', end='')
            for l in range(ord(first) + size - x, ord(last) + 1):
                if (ord(first) + size - x == ord(first) + 1 and l == ord(last)):
                    print(chr(l) + '', end='')        
                else:
                    print(chr(l) + '-', end='')    
        else:
            for l in range(ord(last), ord(first) + size - 2 - (2*size-2 - x), -1):
                print(chr(l) + '-', end='')
            for l in range(ord(first) + size - (2*size-2 - x), ord(last) + 1):
                print(chr(l) + '-', end='')    
        for y in range(2*size-2 - 2*x - 1):
            print('-', end='')
        for y in range(2*size-2 - 2*x + 1, 0):
            print('-', end='')
        print('')
        

