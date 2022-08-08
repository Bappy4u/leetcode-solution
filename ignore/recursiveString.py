def reverseString(s, i=0):
    if i<len(s):
        reverseString(s, i+1)
        print(s[i], end="")
    else:
        return

    


reverseString("bappy")
