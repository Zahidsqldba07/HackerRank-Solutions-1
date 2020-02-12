def count_substring(string, sub_string):
    counter = 0
    position = 0
    while position < len(string):
        # print(str(position) + ":" + string[position:] + "=" + str(string[position:].find(sub_string)))
        if string[position:].find(sub_string) >= 0:
            position+=string[position:].find(sub_string)+1
            counter+=1
        else:
            position=len(string)
    return counter

