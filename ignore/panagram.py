def isPanagram(s:str) -> bool:
    dic = {}
    s = s.lower()
    for c in s:
        if c !=" ":
            dic[c] = None

    print(dic)
    return len(dic)==26


print(isPanagram("The quick brown fox jumps over the lazzy dog"))