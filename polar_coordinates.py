from cmath import phase


def coordinates(number):
    complex_num = complex(number)
    absolute = abs(complex_num)
    phi = phase(complex_num)
    print(absolute)
    print(phi)


if __name__ == "__main__":
    number = input()
    coordinates(number)
