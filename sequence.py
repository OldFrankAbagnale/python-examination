# Вычисление ex. Вычисление ряда 1 + x + x2/2! + x3/3! + … для
# заданного аргумента x с заданной точностью eps (т.е. остановить
# вычисление, когда xk/k! по модулю будет меньше eps). Постараться
# выполнять вычисления наиболее эффективно.
# Исходные данные:
# 1 0.001
# Результат:
# 2.718
import math

def solution(x,eps):
    reslut=1.0 #result
    term=1.0
    k=0             # used for factorial
    factorial=1     #переменная factorial добавлена в попытке повысить читаемость кода

    while (term)>eps:                     # 1 + x + x2/2! + x3/3! + …
        k += 1
        term *= (x / k)
        reslut += term
        #print("iteration:",k,"term is", term,"factorial is ",factorial)
        #print("iteration:", k, "(x / factorial) ==",(x / factorial))
    return reslut












