while True:
    try:
        n = int(input("Введите число n: "))

        for i in range(n):
            row = ''
            for j in range(i + 1):
                row += str(j + 1)
            print(row)
        exit()
    except Exception as e:
        print("Ошибка: ", e)
