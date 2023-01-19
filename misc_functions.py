def bck_spc(string):
    splitlist = list(string)
    splitlist.pop()
    str1 = ""
    for ele in splitlist:
        str1 += ele
    return str1.strip()

def delete(string):
    splitlist = list(string)
    splitlist.pop(len(splitlist)-(len(splitlist)))
    str1 = ""
    for ele in splitlist:
        str1 += ele
    return str1.strip()

string="hello by idris vohra"
print(bck_spc(string))
print(delete(string))
# print(CamelCase(string))