# Complete the solve function below.
def capitalize(word):
    word = word[0].upper() + word[1:]
    return word


def lowerz(word):
    return word.lower()


def solve(s):
    words = s.split()
    capitalized = list(map(capitalize, words))
    for capital in capitalized:
        lower = lowerz(capital)
        s = s.replace(lower, capital)
    print(s)


if __name__ == '__main__':

    s = input()

    result = solve(s)
