s = "madama"
t = ""

# one way

if s == s[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")



# another way
    

#another way

for n in range(len(s)//2):
    if s[n] != s[len(s)-n-1]:
        print("its not a palindrome")
        break

else:
    print("its a palidrome")

    
