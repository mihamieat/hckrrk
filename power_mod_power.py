def result(a, b, m):
    power = pow(a,b)
    modulo = pow(a,b, m)
    print(power)
    print(modulo)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    result(a,b,m)