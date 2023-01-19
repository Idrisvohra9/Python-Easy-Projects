import os
os.system("cls")
user_input=input("Enter text to see what it is: ")
split= user_input.split()

for i in range(len(split)):
    # split[i] = str(split[i])

    if split[i].isalpha():
        print(f"{split[i]} : string.")
    
    elif split[i].isdigit():
        print(f"{split[i]} : integer.")

    else :
        split[i]=float(split[i])
        check_float= isinstance(split[i],float)
        if check_float==True:
            print(f"{split[i]} : float.")