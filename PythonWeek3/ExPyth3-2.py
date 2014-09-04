def sieve(n): #По шагам алгоритма Эратосфена: 
    just = list(range(2,n+1)) 
    pr = 2
    result = [2,]
    while pr <= n: #Убираем из нашего списка все числа 
        just = [numb for numb in just if numb not in range(pr,n+1,pr)] #с шагом pr - все делимые на pr числа
        if just != []: # и добавляем первое число - простое - в результат
            pr = just[0] #костылём убираем добавление пустого списка
            result.append(pr)
        else:
            break
    return result
