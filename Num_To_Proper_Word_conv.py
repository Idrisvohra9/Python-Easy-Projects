input = input("Enter a number: ")

split = input.split(sep=",")

pref = ["", "Hundred ", "Thousand ", "Lakh "]
unit = [
    "",
    "One ",
    "Two ",
    "Three ",
    "Four ",
    "Five ",
    "Six ",
    "Seven ",
    "Eight ",
    "Nine ",
]
tens = [
    "",
    "Ten ",
    "Twenty ",
    "Thirty ",
    "Fourty ",
    "Fifty ",
    "Sixty ",
    "Seventy ",
    "Eighty ",
    "Ninety ",
]
el_l = [
    "",
    "Eleven ",
    "Twelve ",
    "Thirteen ",
    "Fourteen ",
    "Fifteen ",
    "Sixteen ",
    "Seventeen ",
    "Eighteen ",
    "Nineteen ",
]

# The numbers from 1,000,000 to Less than or equal to 9,999,999:
# The numbers from 1,00,000 to Less than or equal to 9,99,999:
if len(input) == 8:
    for i in range(len(split)):
        while i == 0:
            f_d = int(split[0])
            d1 = unit[f_d]
            prefx = pref[3]
            if f_d == 0:
                prefx = pref[0]
            print(f"==> {d1}{prefx}", end="")
            break
        while i == 1:
            s_d = int(split[1])
            pref2 = tens[0]
            prefx = pref[2]
            eleven = el_l[0]
            s_sd = int(split[1][1])
            d2 = unit[s_sd]
            if s_d == 00:
                prefx = pref[0]
            elif s_d == 10:
                pref2 = tens[1]
            elif s_d > 19 and s_d <= 29:
                pref2 = tens[2]
            elif s_d > 29 and s_d <= 39:
                pref2 = tens[3]
            elif s_d > 39 and s_d <= 49:
                pref2 = tens[4]
            elif s_d > 49 and s_d <= 59:
                pref2 = tens[5]
            elif s_d > 59 and s_d <= 69:
                pref2 = tens[6]
            elif s_d > 69 and s_d <= 79:
                pref2 = tens[7]
            elif s_d > 79 and s_d <= 89:
                pref2 = tens[8]
            elif s_d > 89 and s_d <= 99:
                pref2 = tens[9]

            if s_d == 11:
                eleven = el_l[1]
                d2 = unit[0]
            if s_d == 12:
                eleven = el_l[2]
                d2 = unit[0]
            if s_d == 13:
                eleven = el_l[3]
                d2 = unit[0]
            if s_d == 14:
                eleven = el_l[4]
                d2 = unit[0]
            if s_d == 15:
                eleven = el_l[5]
                d2 = unit[0]
            if s_d == 16:
                eleven = el_l[6]
                d2 = unit[0]
            if s_d == 17:
                eleven = el_l[7]
                d2 = unit[0]
            if s_d == 18:
                eleven = el_l[8]
                d2 = unit[0]
            if s_d == 19:
                eleven = el_l[9]
                d2 = unit[0]

            print(f"{pref2}{d2}{eleven}{prefx}", end="")
            break

        while i == 2:
            t_d = int(split[2][0])
            t_sd = int(split[2][1:3])
            d3 = unit[t_d]
            t_td = int(split[2][2])
            eleven = el_l[0]
            d4 = unit[t_td]
            pref3 = tens[0]
            prefx = pref[1]

            if t_d == 0:
                prefx = pref[0]
            elif t_sd == 10:
                pref3 = tens[1]
            elif t_sd > 19 and t_sd <= 29:
                pref3 = tens[2]
            elif t_sd > 29 and t_sd <= 39:
                pref3 = tens[3]
            elif t_sd > 39 and t_sd <= 49:
                pref3 = tens[4]
            elif t_sd > 49 and t_sd <= 59:
                pref3 = tens[5]
            elif t_sd > 59 and t_sd <= 69:
                pref3 = tens[6]
            elif t_sd > 69 and t_sd <= 79:
                pref3 = tens[7]
            elif t_sd > 79 and t_sd <= 89:
                pref3 = tens[8]
            elif t_sd > 89 and t_sd <= 99:
                pref3 = tens[9]

            if t_sd == 11:
                eleven = el_l[1]
                d4 = unit[0]
            if t_sd == 12:
                eleven = el_l[2]
                d4 = unit[0]
            if t_sd == 13:
                eleven = el_l[3]
                d4 = unit[0]
            if t_sd == 14:
                eleven = el_l[4]
                d4 = unit[0]
            if t_sd == 15:
                eleven = el_l[5]
                d4 = unit[0]
            if t_sd == 16:
                eleven = el_l[6]
                d4 = unit[0]
            if t_sd == 17:
                eleven = el_l[7]
                d4 = unit[0]
            if t_sd == 18:
                eleven = el_l[8]
                d4 = unit[0]
            if t_sd == 19:
                eleven = el_l[9]
                d4 = unit[0]

            print(f"{d3}{prefx}{eleven}{pref3}{d4}/-")
            break

# The numbers from 10,000 to Less than or equal to 99,999:
if len(input) == 6:
    for i in range(len(split)):
        while i == 0:
            s_d = int(split[0])
            pref2 = tens[0]
            prefx = pref[2]
            eleven = el_l[0]
            s_sd = int(split[0][1])
            d2 = unit[s_sd]
            if s_d == 0:
                prefx = pref[0]
            elif s_d == 10:
                pref2 = tens[1]
            elif s_d > 19 and s_d <= 29:
                pref2 = tens[2]
            elif s_d > 29 and s_d <= 39:
                pref2 = tens[3]
            elif s_d > 39 and s_d <= 49:
                pref2 = tens[4]
            elif s_d > 49 and s_d <= 59:
                pref2 = tens[5]
            elif s_d > 59 and s_d <= 69:
                pref2 = tens[6]
            elif s_d > 69 and s_d <= 79:
                pref2 = tens[7]
            elif s_d > 79 and s_d <= 89:
                pref2 = tens[8]
            elif s_d > 89 and s_d <= 99:
                pref2 = tens[9]

            if s_d == 11:
                eleven = el_l[1]
                d2 = unit[0]
            if s_d == 12:
                eleven = el_l[2]
                d2 = unit[0]
            if s_d == 13:
                eleven = el_l[3]
                d2 = unit[0]
            if s_d == 14:
                eleven = el_l[4]
                d2 = unit[0]
            if s_d == 15:
                eleven = el_l[5]
                d2 = unit[0]
            if s_d == 16:
                eleven = el_l[6]
                d2 = unit[0]
            if s_d == 17:
                eleven = el_l[7]
                d2 = unit[0]
            if s_d == 18:
                eleven = el_l[8]
                d2 = unit[0]
            if s_d == 19:
                eleven = el_l[9]
                d2 = unit[0]

            print(f"==> {pref2}{d2}{eleven}{prefx}", end="")
            break

        while i == 1:
            t_d = int(split[1][0])
            t_sd = int(split[1][1:3])
            d3 = unit[t_d]
            t_td = int(split[1][2])
            eleven = el_l[0]
            d4 = unit[t_td]
            pref3 = tens[0]
            prefx = pref[1]

            if t_d == 0:
                prefx = pref[0]
            elif t_sd == 10:
                pref3 = tens[1]
            elif t_sd > 19 and t_sd <= 29:
                pref3 = tens[2]
            elif t_sd > 29 and t_sd <= 39:
                pref3 = tens[3]
            elif t_sd > 39 and t_sd <= 49:
                pref3 = tens[4]
            elif t_sd > 49 and t_sd <= 59:
                pref3 = tens[5]
            elif t_sd > 59 and t_sd <= 69:
                pref3 = tens[6]
            elif t_sd > 69 and t_sd <= 79:
                pref3 = tens[7]
            elif t_sd > 79 and t_sd <= 89:
                pref3 = tens[8]
            elif t_sd > 89 and t_sd <= 99:
                pref3 = tens[9]

            if t_sd == 11:
                eleven = el_l[1]
                d4 = unit[0]
            if t_sd == 12:
                eleven = el_l[2]
                d4 = unit[0]
            if t_sd == 13:
                eleven = el_l[3]
                d4 = unit[0]
            if t_sd == 14:
                eleven = el_l[4]
                d4 = unit[0]
            if t_sd == 15:
                eleven = el_l[5]
                d4 = unit[0]
            if t_sd == 16:
                eleven = el_l[6]
                d4 = unit[0]
            if t_sd == 17:
                eleven = el_l[7]
                d4 = unit[0]
            if t_sd == 18:
                eleven = el_l[8]
                d4 = unit[0]
            if t_sd == 19:
                eleven = el_l[9]
                d4 = unit[0]

            print(f"{d3}{prefx}{eleven}{pref3}{d4}/-")
            break

# The numbers from 1,000 to Less than or equal to 9,999:
if len(input) == 5:
    for i in range(len(split)):
        while i == 0:
            f_d = int(split[0])
            d1 = unit[f_d]
            prefx = pref[2]
            if f_d == 0:
                prefx = pref[0]
            print(f"==> {d1}{prefx}", end="")
            break
        while i == 1:
            t_d = int(split[1][0])
            t_sd = int(split[1][1:3])
            d3 = unit[t_d]
            t_td = int(split[1][2])
            eleven = el_l[0]
            d4 = unit[t_td]
            pref3 = tens[0]
            prefx = pref[1]

            if t_d == 0:
                prefx = pref[0]
            elif t_sd == 10:
                pref3 = tens[1]
            elif t_sd > 19 and t_sd <= 29:
                pref3 = tens[2]
            elif t_sd > 29 and t_sd <= 39:
                pref3 = tens[3]
            elif t_sd > 39 and t_sd <= 49:
                pref3 = tens[4]
            elif t_sd > 49 and t_sd <= 59:
                pref3 = tens[5]
            elif t_sd > 59 and t_sd <= 69:
                pref3 = tens[6]
            elif t_sd > 69 and t_sd <= 79:
                pref3 = tens[7]
            elif t_sd > 79 and t_sd <= 89:
                pref3 = tens[8]
            elif t_sd > 89 and t_sd <= 99:
                pref3 = tens[9]

            if t_sd == 11:
                eleven = el_l[1]
                d4 = unit[0]
            if t_sd == 12:
                eleven = el_l[2]
                d4 = unit[0]
            if t_sd == 13:
                eleven = el_l[3]
                d4 = unit[0]
            if t_sd == 14:
                eleven = el_l[4]
                d4 = unit[0]
            if t_sd == 15:
                eleven = el_l[5]
                d4 = unit[0]
            if t_sd == 16:
                eleven = el_l[6]
                d4 = unit[0]
            if t_sd == 17:
                eleven = el_l[7]
                d4 = unit[0]
            if t_sd == 18:
                eleven = el_l[8]
                d4 = unit[0]
            if t_sd == 19:
                eleven = el_l[9]
                d4 = unit[0]

            print(f"{d3}{prefx}{eleven}{pref3}{d4}/-")
            break

# The numbers from 100 to Less than or equal to 999:
if len(input) == 3:
    for i in range(len(split)):
        while i == 0:
            t_d = int(split[0][0])
            t_sd = int(split[0][1:3])
            d3 = unit[t_d]
            t_td = int(split[0][2])
            eleven = el_l[0]
            d4 = unit[t_td]
            pref3 = tens[0]
            prefx = pref[1]

            if t_d == 0:
                prefx = pref[0]
            elif t_sd == 10:
                pref3 = tens[1]
            elif t_sd > 19 and t_sd <= 29:
                pref3 = tens[2]
            elif t_sd > 29 and t_sd <= 39:
                pref3 = tens[3]
            elif t_sd > 39 and t_sd <= 49:
                pref3 = tens[4]
            elif t_sd > 49 and t_sd <= 59:
                pref3 = tens[5]
            elif t_sd > 59 and t_sd <= 69:
                pref3 = tens[6]
            elif t_sd > 69 and t_sd <= 79:
                pref3 = tens[7]
            elif t_sd > 79 and t_sd <= 89:
                pref3 = tens[8]
            elif t_sd > 89 and t_sd <= 99:
                pref3 = tens[9]

            if t_sd == 11:
                eleven = el_l[1]
                d4 = unit[0]
            if t_sd == 12:
                eleven = el_l[2]
                d4 = unit[0]
            if t_sd == 13:
                eleven = el_l[3]
                d4 = unit[0]
            if t_sd == 14:
                eleven = el_l[4]
                d4 = unit[0]
            if t_sd == 15:
                eleven = el_l[5]
                d4 = unit[0]
            if t_sd == 16:
                eleven = el_l[6]
                d4 = unit[0]
            if t_sd == 17:
                eleven = el_l[7]
                d4 = unit[0]
            if t_sd == 18:
                eleven = el_l[8]
                d4 = unit[0]
            if t_sd == 19:
                eleven = el_l[9]
                d4 = unit[0]

            print(f"==> {d3}{prefx}{eleven}{pref3}{d4}/-")
            break

# The numbers from 10 to Less than or equal to 99:
if len(input) == 2:
    for i in range(len(split)):
        while i == 0:
            s_d = int(split[0])
            pref2 = tens[0]
            eleven = el_l[0]
            s_sd = int(split[0][1])
            d2 = unit[s_sd]

            if s_d == 10:
                pref2 = tens[1]
            elif s_d > 19 and s_d <= 29:
                pref2 = tens[2]
            elif s_d > 29 and s_d <= 39:
                pref2 = tens[3]
            elif s_d > 39 and s_d <= 49:
                pref2 = tens[4]
            elif s_d > 49 and s_d <= 59:
                pref2 = tens[5]
            elif s_d > 59 and s_d <= 69:
                pref2 = tens[6]
            elif s_d > 69 and s_d <= 79:
                pref2 = tens[7]
            elif s_d > 79 and s_d <= 89:
                pref2 = tens[8]
            elif s_d > 89 and s_d <= 99:
                pref2 = tens[9]

            if s_d == 11:
                eleven = el_l[1]
                d2 = unit[0]
            if s_d == 12:
                eleven = el_l[2]
                d2 = unit[0]
            if s_d == 13:
                eleven = el_l[3]
                d2 = unit[0]
            if s_d == 14:
                eleven = el_l[4]
                d2 = unit[0]
            if s_d == 15:
                eleven = el_l[5]
                d2 = unit[0]
            if s_d == 16:
                eleven = el_l[6]
                d2 = unit[0]
            if s_d == 17:
                eleven = el_l[7]
                d2 = unit[0]
            if s_d == 18:
                eleven = el_l[8]
                d2 = unit[0]
            if s_d == 19:
                eleven = el_l[9]
                d2 = unit[0]

            print(f"==> {pref2}{d2}{eleven}/-", end="")
            break

# The numbers from 0 to Less than or equal to 9:
if len(input) == 1:
    for i in range(len(split)):
        while i == 0:
            f_d = int(split[0])
            d1 = unit[f_d]
            prefx = pref[0]
            if f_d == 0:
                d1 = unit[0]
                prefx = "Zero"
            print(f"==> {d1}{prefx}/-", end="")
            break
