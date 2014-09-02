def chr_to_num(x):
  x = ord(x)
  if ord("0") <= x <= ord("9"): return x - ord("0")
  elif ord("a") <= x <= ord("z"): return x - ord("a") + 10
  else: return x - ord("A") + 10
def hex_to_hep(x):
    coef = []
    x = list(x)
    for i in range(len(x)):
        x[i]=chr_to_num(x[i])
        coef.append(x[i])
    prom = 0
    for i in range(len(coef)):#во избежание заморочек
        prom += coef[i] * (16**(len(coef)-i-1))#получим из 16-чной 
    coef_res = [] #сначала число
    while prom > 7:#а уже из него - строку в 7-чной системе
        coef_res.append(str(prom%7))
        prom = prom//7
    coef_res.append(str(prom%7))
    coef_res = reversed(coef_res)
    result = "".join(coef_res)
    return(result) 
