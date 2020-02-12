

# Complete the solve function below.
def solve(s):
    previous = None
    result = ""
    for c in s:
        if previous == None or previous == " ":
            c = c.upper()
        previous = c
        result = result + c
    return result

