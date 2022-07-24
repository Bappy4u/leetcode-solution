
def makeFancyString(s: str) -> str:
    l = len(s)
    news = ""
    count = 0
    i = 0
    while i < l - 1:

        if s[i] == s[i + 1]:
            count += 1
        else:
            count = 0
        if count >= 2:
            pass
        else:
            news += s[i]
        i += 1

    news += s[-1]
    return news


res = makeFancyString("Bapppy")
print(res)

