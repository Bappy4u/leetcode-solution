"""
*..
**.
***
"""
for i in range(3):
    for j in range(3):
        if j <= i:
            print("*", end="")
        else:
            print(".", end="")

    print("")


print("-----------------")
for i in range(3):
    for j in range(3):
        if i+j < 3:
            print("*", end="")
        else:
            print(".", end="")

    print("")


print("-----------------")
for i in range(3):
    for j in range(3):
        if i+j < 3:
            print("*", end="")
        else:
            print(".", end="")

    print("")