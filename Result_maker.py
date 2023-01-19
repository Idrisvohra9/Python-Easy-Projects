eng = float(input("ENG->"))
guj = float(input("GUJ->"))
hin = float(input("HIN->"))
sci = float(input("SCIENCE->"))
s_s = float(input("SOCIAL SCI->"))
maths = float(input("MATHS->"))
comp = float(input("COMPUTER->"))
n = eng + guj + hin + sci + s_s + maths + comp
grade = (n) / 7
if grade >= 40:
    G="PASS"
else:
    G="FAIL"
print("Grade :",G)
percent = float((n/700)*100)
print("percentage->", percent)
