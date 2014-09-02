def is_number(x):
    x = str(x)
    result = False
    commacntr = 0 #количество встреченных в строке запятых
    for i in range(len(x)): #простая посимвольная проверка
        if x[0] == "-": #для выявления
            result = True #отрицательных чисел
        elif x[i] == "." or x[i] == ",":
            commacntr += 1
            if commacntr > 1:
                result = False
                break
            else:
                continue
        elif x[i].isdigit():
            result = True
        else:
            result = False
            break
    return result

