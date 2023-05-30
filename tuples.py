if __name__ == "__main__":
    N = int(input())
    my_ints = input().split()
    my_ints = list(map(int, my_ints))

    my_tuple = tuple(my_ints)
    my_hash = hash(my_tuple)

    print(my_hash)
