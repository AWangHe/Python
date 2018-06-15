# -*- coding: utf-8 -*-
import re
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39" and str[1:3] != "31":
        return False
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False
        
    return True

def checkPhone2(str):
    #13912345678
    pat = r"(1(([3578]\d)|(47))\d{8})"
    res = re.findall(pat, str)
    print(res)

'''    
print(checkPhone2("13912345678"))
print(checkPhone2("139123456783"))
print(checkPhone2("1391234567"))
print(checkPhone2("23912345678"))
print(checkPhone2("13912a45678"))
'''

str = "abcdef13123456789hafduajugdja15123456789"

checkPhone2(str)




re_QQ = re.compile(r"^[1-9]\d{5,9}$")


















