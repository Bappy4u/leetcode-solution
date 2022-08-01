def reverse1(word: str):
    return "".join(reversed(list(word)))



def reverseSent(words):
    temp = ""
    res = ""
    for c in words:
        temp +=c
        if c == " ":
            res = temp + res
        
    return res

print(reverseSent("hello world!"))