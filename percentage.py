if __name__ == "__main__":
    n = int(input("number of students:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("student name:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("student query:")
    result = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("%.2f" % result)