def reverse1(word: str):
    return "".join(reversed(list(word)))



def reverseSent(words):
    temp = " "
    res = ""
    for c in words:
        print(c)
        temp +=c
        if c == " ":
            res = temp +" "+ res
            temp =""
    res = temp + res 
    return res

print(reverseSent("I love you."))

