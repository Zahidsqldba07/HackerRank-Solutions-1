if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ar = []
    for xi in range(x+1):
        for yi in range(y+1):
            for zi in range(z+1):
                if (xi+yi+zi != n):
                    ar.append([xi, yi, zi])
                    
    print(ar)
