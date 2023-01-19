while True:
    inp = input("Enter a correct Ip Address: ")
    splitter = inp.split(".")
    # 127.45.278.190.20
    unlock = 0
    if len(splitter) == 5:
        for i in range(0, len(splitter)):
            splitter[i] = int(splitter[i])

        if splitter[0] >= 200:
            print("Enter a correct Ip Address.")

        else:
            unlock += 1

        if splitter[1] >= 100:
            print("Enter a correct Ip Address.")

        else:
            unlock += 1

        if splitter[2] < 200 or splitter[2] >= 300:
            print("Enter a correct Ip Address.")

        else:
            unlock += 1

        if splitter[3] <= 150 and splitter[3] > 200:
            print("Enter a correct Ip Address.")

        else:
            unlock += 1

        if splitter[4] <= 19 and splitter[4] > 20:
            print("Enter a correct Ip Address.")

        else:
            unlock += 1

    else:
        print("IP address should contain atleast 5 dots.")

    if unlock == 5:
        print("Welcome captain!")
        False
