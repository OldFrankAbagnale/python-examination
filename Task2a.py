text = "Гречка и Монеточка устроились певицами."
def reverser(text):
    # text = input()  # Чтобы ввести с консоли
    text=text.split()  # Разделяем

    reslut=[] #список
    for item in text:
        item=item[::-1] #разворот
        #print(item)
        reslut.append(item) #добавляем в список

    #print(isinstance(reslut, list))
    #print(reslut)

    return str(reslut)
def main():
   print(reverser(text))
if __name__ == '__main__':
    main()


