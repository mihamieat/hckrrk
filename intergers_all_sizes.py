def operation(a, b, c, d):
    result = a ** b + c ** d
    return result

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(operation(a, b, c, d))