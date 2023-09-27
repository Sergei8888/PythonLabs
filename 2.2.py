while True:
    try:
        n = int(input("Введите число n: "))

        maxRowLength = 0
        for i in range(n):
            maxRowLength += len(str(i + 1))
        maxRowLength *= 2
        maxRowLength -= 1

        for i in range(n):
            row = ''
            for j in range(i, 0, -1):
                row += str(j + 1)
            for j in range(i + 1):
                row += str(j + 1)
            spacesNeeded = maxRowLength - len(row)
            spacedExpected = maxRowLength - (len(row) - n) * 2
            maxRowLength - len(row)
            print(' ' * int((spacesNeeded / 2)) + row + ' ' * int((spacesNeeded / 2)))

        exit()
    except Exception as e:
        print("Ошибка:", e)
