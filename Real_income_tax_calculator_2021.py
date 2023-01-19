income=(float(input("Enter your income in lacs\n")))
if income<=250000:
    print("Nil.")
if income>=250000 and income<=500000:
    tax=0.05*(income-250000)
if income>=500000 and income<=750000:
    tax=12500+0.1*(income-500000)
if income>=750000 and income<=1000000:
    tax=37500+0.15*(income-750000)
if income>=1000000 and income<=1250000:
    tax=75000+0.20*(income-1000000)
if income>=1250000 and income<=1500000:
    tax=125000+0.25*(income-1250000)
if income>1500000:
    tax=187500+0.3*(income-1500000)
    print("Your income for this month will be",tax,"rs.")
    