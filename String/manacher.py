def manacher(s: str) -> list:
    """
    fuction will return the index of largest palindrome present inside
    string
    (strart_index, end_index+1)
    >>> manacher("a")
    (0,1)
    """
    if s == "":
        return (0, 1)
    t = "^#" + "#".join(s) + "#$"
    c = 1  # center of palindrome
    d = 1  # rightest index of c center palindrome
    P = [0] * len(t)
    for i in range(2, len(t) - 1):
        # mirror index calculation using C
        mirror = 2 * c - i
        P[i] = max(
            0, min(d - i, P[mirror])
        )  # precalculted value of palindrome using mirror
        while (
            t[i + 1 + P[i]] == t[i - 1 - P[i]]
        ):  # increase radious of palindrome if exist
            P[i] += 1
        if (
            i + P[i] > d
        ):  # if current palindrome become rightest palindrome then update c and d
            c = i
            d = i + P[i]
    k, i = max((P[i], i) for i in range(1, len(t) - 1))
    return ((i - k) // 2, (i + k) // 2)


if __name__ == "__main__":
    print(manacher("rachelhellabracadabra"))
