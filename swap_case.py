def swap_case(s):
    swap_list = [i.lower() if i.isupper() else i.upper() for i in s]
    result = "".join(swap_list)
    return result


if __name__ == '__main__':
    s = input()
    print(swap_case(s))
