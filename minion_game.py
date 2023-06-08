def minion_game(string):
    vowels = list('aeiouy')
    tmp_words = []
    all_words = []

    for i in range(len(string)):
        word = string[i:]
        tmp_words.append(word)

    for word in tmp_words:
        for i in range(len(word)):
            wordi = word[:i+1]
            all_words.append(wordi)

    kevin_words = [w for w in all_words if w[0].lower() in vowels]
    stuart_words = [w for w in all_words if w[0].lower() not in vowels]

    if len(kevin_words) > len(stuart_words):
        print(f"Kevin {len(kevin_words)}")
    elif len(kevin_words) == len(stuart_words):
        print("Draw")
    else:
        print(f"Stuart {len(stuart_words)}")


if __name__ == '__main__':
    string = input()
    minion_game(string)
