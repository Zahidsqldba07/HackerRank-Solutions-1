if __name__ == '__main__':
    N = int(input())
    ls = []

    for i in range(N):
        command = input()
        if command.startswith("insert"):
            ls.insert(int(command.split()[1]), int(command.split()[2]))
        elif command.startswith("print"):
            print(ls)
        elif command.startswith("remove"):
            ls.remove(int(command.split()[1]))
        elif command.startswith("append"):
            ls.append(int(command.split()[1]))
        elif command.startswith("sort"):
            ls.sort()
        elif command.startswith("pop"):
            ls.pop()
        elif command.startswith("reverse"):
            ls.reverse()


        
