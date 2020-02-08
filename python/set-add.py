# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
countries = set()

for i in range(int(n)):
    data = input()
    countries.add(data)

print(len(list(countries)))
