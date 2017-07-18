# Source: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def ransom_note(magazine, ransom):
    mag_words = {}
    for word in magazine:
        if word not in mag_words:
            mag_words[word] = 1
        else:
            mag_words[word] += 1

    for word in ransom:
        if word not in mag_words or mag_words[word] is 0:
            return False
        else:
            mag_words[word] -= 1
    return True
