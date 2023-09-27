while True:
    try:
        a, b, c = map(int, input("Введите три числа через пробел: ").split())

        if a == b == c:
            print(3)
            exit()

        if a == b or a == c or b == c:
            print(2)
            exit()

        print(0)
        exit()
    except Exception as e:
        print("Ошибка: ", e)
