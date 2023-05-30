if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
    my_list.sort(reverse=True)
    my_list = list(dict.fromkeys(my_list))
    print(my_list[1])
