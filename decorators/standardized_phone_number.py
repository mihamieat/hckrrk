def wrapper(f):
    def fun(input_number):
        ten_digit_numbers = [i[-10:-5] + " " + i[-5:] for i in input_number]
        numbers_plus91 = ["+91 " + item for item in ten_digit_numbers]
        f(numbers_plus91)

    return fun


@wrapper
def sort_phone(input_number):
    print(*sorted(input_number), sep="\n")


if __name__ == "__main__":
    input_number = [input() for _ in range(int(input()))]
    sort_phone(input_number)
