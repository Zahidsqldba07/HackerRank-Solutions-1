if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_marks = 0.0
    for mark in student_marks[query_name]:
        sum_marks += mark

    average = sum_marks/len(student_marks[query_name])
    print("%.2f" % average)
    # print(reduce(lambda x, y: x + y, student_marks[query_name]) / len(student_marks[query_name])))
