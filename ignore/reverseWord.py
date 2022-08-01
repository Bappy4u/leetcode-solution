def reverse1(word: str):
    return "".join(reversed(list(word)))


def reverse2(words):
    res = ""

    for c in words:
        res = c + res

    return res

def reverseSent(words):
    temp = " "
    res = ""
    for c in words:
        print(c)
        temp +=c
        if c == " ":
            res = temp +" "+ res
            temp =" "
    res = temp + res 
    return res

print(reverseSent("I love you."))

print(reverse2("I eat rice."))

