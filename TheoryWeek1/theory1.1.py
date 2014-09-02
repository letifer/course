def chr_to_num(x):
  x = ord(x)
  if ord("0") <= x <= ord("9"): return x - ord("0")
  elif ord("a") <= x <= ord("z"): return x - ord("a") + 10
  else: return x - ord("A") + 10
def oct_to_dec(x):
    coef = []
    x = list(x)
    for i in range(len(x)):#превращем строку на входе
        x[i]=chr_to_num(x[i]) #в список цифр в 8-й 
        coef.append(x[i]) #системе
    result = 0
    for i in range(len(coef)): #используя их в качестве коэф-в
        result += coef[i] * (8**(len(coef)-i-1))#получаем число
    return result
