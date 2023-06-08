if __name__ == "__main__":
    N = int(input())
    records = []
    for _ in range(N):
        name = input()
        mark = float(input())
        records.append([name, mark])

    marks = [record[1] for record in records]
    marks.sort()
    marks = list(dict.fromkeys(marks))
    second_lower_score = marks[1]
    second_lower_scorrers = [
        record[0] for record in records if record[1] == second_lower_score
    ]
    second_lower_scorrers.sort()
    for student in second_lower_scorrers:
        print(student)
