# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
mset = input()
n = input()
nset = input()

a = set(map(int, mset.split()))
b = set(map(int, nset.split()))

print(str(len(a.union(b))))
