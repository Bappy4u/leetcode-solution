#Ka-123-123
#Kha-12-312
#Gha-123-123

st = "Gha-13-123"



def isNumberValid(number) -> str:
    arrOfnumber = number.split("-")
    if len(arrOfnumber) !=3:
        return False
    dic = {
        "ka": 1,
        "kha": 1,
        "ga": 1,
        "gha": 1
    }
    
    n1 = arrOfnumber[0].lower()
    n2 = arrOfnumber[1]
    n3 = arrOfnumber[2]

    if not dic.get(n1):
        return False
    
    if len(n2)>3 and len(n2)<2 and len(n3)>3 and len(n3)<2:
        return False
    
    if  not n2.isdigit() and not n3.isdigit() :

        return False
    
    return False



print(isNumberValid(st))

