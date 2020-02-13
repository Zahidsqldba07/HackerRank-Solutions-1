def print_odd_even(param):
    str_odd = "";
    str_even = "";
    for i in range(len(param)):
        if i % 2 == 0:
            str_odd += param[i]
        else:
            str_even += param[i]
    print(str_odd + " " + str_even)

t = int(input())
for i in range(0, t):
    param=input()
    print_odd_even(param)