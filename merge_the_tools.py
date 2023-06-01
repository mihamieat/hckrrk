import itertools


def merge_the_tools(string, k):
    n = k / len(string)
    n = int(n)
    print(n)
    separated_strings = [string[i:i+n] for i in range(0, len(string), n)]
    for group in separated_strings:
        result = ''.join(ch for ch, _ in itertools.groupby(group))
        print(result)


if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
