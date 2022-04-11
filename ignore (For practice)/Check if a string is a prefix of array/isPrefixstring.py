from typing import List


def isPrefixString(s: str, words: List[str]) -> bool:
    news = s
    l = len(s)
    for word in words:
        if l <= 0:
            return True
        else:
            if news.startswith(word):
                news = news[len(word):]
                l = l - len(word)
            else:
                return False

    if l == 0:
        return True
    else:
        return False


res = isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"])

print(res)