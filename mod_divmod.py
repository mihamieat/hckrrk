def divmods(a, b):
    result = divmod(a, b)
    for outcome in result:
        print(outcome)
    print(result)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    divmods(a, b)
