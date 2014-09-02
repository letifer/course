def input_int(a,b):
    while True:
        x=input("Введите проверяемое число: ")
        if x.isdigit():
            if x >=a and x <= b:
                return True
                break
            else:
                print("Повторите попытку")
                continue
        else:
            print("Повторите попытку")
            continue
