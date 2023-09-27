while True:
    try:
        n = int(input("Введите число n: "))

        for i in range(n):
            for j in range(i + 1):
                print(j + 1, end="")
            print('')
        exit()
    except Exception as e:
        print("Ошибка: ", e)
