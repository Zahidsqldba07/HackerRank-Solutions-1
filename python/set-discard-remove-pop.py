n = int(input())
s = set(map(int, input().split()))
k = int(input())

for i in range(k):
    data = input().split()
    if len(data) == 2:
        if data[0] == "remove":
            s.remove(int(data[1]))
        elif data[0] == "discard":
            s.discard(int(data[1]))
    else:
        if data[0] == "pop":
            s.pop()

print(sum(s))
