def is_number(x):
    x = str(x)
    result = False
    commacntr = 0 #количество встреченных в строке запятых
    for i in range(len(x)): #простая посимвольная проверка
        if x == "-0":
            break
        elif x[0].isdigit() or x[0] == "-":
            if x[i] == "," or x[i] == ".":
                commacntr += 1
                if commacntr > 1:
                    break
                else:
                    continue
            elif x[i].isdigit():
                result = True
                continue
            else:
                result = False
                break
        else:
            break
    return result

