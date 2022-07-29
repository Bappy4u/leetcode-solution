def multiples(multipleOf, limit):
    firstElement = limit//multipleOf

    for i in range(firstElement, 0, -1):
        print(f"{i*3}, ", end="")



multiples(3, 200)

