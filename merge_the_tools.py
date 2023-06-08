def merge_the_tools(string, k):
    n = len(string) / k + (len(string) % k > 0)
    print(n)
    n = int(n)
    separated_strings = split(string, n)
    for group in separated_strings:
        seen = set()
        new_group_list = [x for x in group if not (x in seen or seen.add(x))]
        result = "".join(new_group_list)
        print(result)


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
