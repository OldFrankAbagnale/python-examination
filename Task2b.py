def reverser(text):
    expr = list(text)     #string to list
    start = 0             #запоминаем начало нового слова
    for i in range(len(expr)):

        if expr[i] == " ":  #идем по тексту, есели видим пробел, разворачиваем слово до него
            expr = expr[:start] + expr[start:i:][::-1] + expr[i:]   #переворачиваем слово
            start = i + 1                                           #запоминаме начало нового слова
    result = str(expr) #list to string
    return result

