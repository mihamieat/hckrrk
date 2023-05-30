if __name__ == "__main__":
    N = int(input())
    records = []
    for _ in range(N):
        name = input()
        mark = float(input())
        records.append([name, mark])

    print(records)
