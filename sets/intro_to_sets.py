def average(array):
    sum_heights = sum(set(array))
    number_of_heights = len(set(array))

    result = sum_heights / number_of_heights

    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
