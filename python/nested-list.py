if __name__ == '__main__':

    students = []
    lowestFirst = -1;
    lowestSecond = -1;

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        if lowestFirst == -1 or lowestFirst > score:
            lowestSecond = lowestFirst
            lowestFirst = score
        elif (lowestSecond == -1 or lowestSecond > score) and lowestFirst < score:
            lowestSecond = score

    selected = []
    for i in range(len(students)):
        if students[i][1] == lowestSecond:
            selected.append(students[i][0])

    selected.sort()
    for i in selected:
        print(i)
    

