# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a = defaultdict(list)
b = []

# nm = input()
# n = int(nm.split()[0])
# m = int(nm.split()[1])
n, m = map(int, input().split())

for i in range(1, n+1):
    a[input()].append(i)
    
for i in range(1, m+1):
    b.append(input())
    
for item in b:
    if item in a:
        # print(*a[item], sep=" ")
        print(" ".join( map(str, a[item]) ))
    else:
        print(-1)
