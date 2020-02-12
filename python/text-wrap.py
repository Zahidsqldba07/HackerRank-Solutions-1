

def wrap(string, max_width):
    c = 0
    result = ""
    while c < len(string):
        # print(str(c) + ":" + string[c], end='')
        result += string[c]
        c+=1
        if (c % max_width == 0):
            # print("")
            result += "\n"
    return result

