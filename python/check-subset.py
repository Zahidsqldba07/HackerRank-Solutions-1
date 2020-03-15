test_cases_number = int(input())

for i in range(test_cases_number):
    a_number = int(input())
    a_set = set(map(int, input().split()))
    b_number = int(input())
    b_set = set(map(int, input().split()))
    
    print(str(a_set.issubset(b_set)))
