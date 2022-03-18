import string


def maximum_border_length(word):
    n, f, k = len(word), [0] * len(word), 0
    for i in range(1, n):
        while word[k] != word[i] and k > 0:
            k = f[k - 1]
        if word[k] == word[i]:
            k += 1
        f[i] = k
    return f


if __name__ == "__main__":
    pattern = "foobarfoo"
    string = "barfoobarfoobarfoobarfoobarfoo"
    f = maximum_border_length(pattern + "#" + string)
    print(f.count(len(pattern)))
