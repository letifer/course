def fibo(n):
    a = 0
    b = 1 
    for i in range(n):
        c = a #Для сохранения промежуточных значений
        a = b
        b += c
    return a

