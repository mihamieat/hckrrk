def sym_diff(a, b):
    set_a = set(list(map(int, a)))
    set_b = set(list(map(int, b)))
    result = sorted(set_a ^ set_b)
    return result


if __name__ == "__main__":
    N = int(input())
    a = set(input().split(" "))
    M = int(input())
    b = set(input().split(" "))
    for line in sym_diff(a, b):
        print(line)
