def maximum_prime(n):
    m = 2
    z = n #используем z, чтобы в дальнейшем сохранить выполнение цикла
    while True:
          if m > z: 
              break
          else:
              if n%m == 0: #Здесь делим на все числа подряд
                  if n == m: #Т.к. простые числа будут удалять
                      break #возможность выдачи сложного делителя
                  else:
                      n //= m
                      continue
              else:
                  m += 1
                  continue
    return m
