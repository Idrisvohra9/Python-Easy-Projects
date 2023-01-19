km = float(input("Enter K.M.:-"))
m = km*1000
cm = km*100000
inch = km*39370.1
ft = km*3281
for_user = str(input("Type of conversion in m / cm / inch / foot-> \n"))

if for_user == "m":
    print(km, "km is equal to", m, "ms")
elif for_user == "cm":
    print(km, "km is equal to", cm, "cms")
elif for_user == "in":
    print(km, "km is equal to", inch, "inchs")
elif for_user == "ft":
    print(km, "km is equal to", ft, "foots")
