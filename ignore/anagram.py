import string
from xmlrpc.client import Boolean


def isAnagram(s1:string, s2:string) -> string:
    if len(s1) != len(s2):
        return False

    s1.lower()
    s2.lower()
    dic = {}
    dic1 = {}
    for i in range(len(s1)):
        dic[s1[i]] = 1 if not dic.get(s1[i]) else dic.get(s1[i]) + 1
        dic1[s2[i]] = 1 if not dic1.get(s2[i]) else dic1.get(s2[i]) + 1
    
    return dic == dic1



print(isAnagram("aacc", "caac"))
