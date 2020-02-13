from sys import stdin

n = input()

phone_book = {}
for i in range(int(n)):
    str = input()
    params = str.split(" ")
    phone_book[params[0]] = params[1]
    
while True:
    try:
        line = input()
    except:
        break
    
    if line in phone_book.keys():
        print(line + "=" + phone_book[line])
    else:
        print("Not found")
    
    