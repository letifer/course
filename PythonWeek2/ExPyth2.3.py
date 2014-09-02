def fibo(n):
    print("Начинаю вычислять " + str(n) +"й член последовательности Фибоначчи")
    if n == 0: result = 0
    elif n == 1: result = 1
    else: result = fibo(n-1) + fibo(n-2)
    print("Вычислил " + str(n) + "й член последовательности Фибоначчи-" + str(result))
    return result
fibo(15)
