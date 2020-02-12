def print_formatted(number):
    space0 = ">" + str(len(format(number, 'b')))
    space1 = ">" + str(len(format(number, 'b')) + 1)
    for i in range(1, 1+number):
        print(format(i, space0 + 'd') + 
              format(i, space1 + 'o') + 
              format(i, space1 + 'X') + 
              format(i, space1 + 'b'))

