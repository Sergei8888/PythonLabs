while True:
    while True:
        try:
            n = int(input("Введите чило n:"))
            result = []
            for i in range(n):
                row = []
                for j in range(i + 1):
                    row.append(j + 1)

                s = ''.join([str(k) for k in row[:-1:]]) + ''.join([str(k) for k in row[::-1]])
                result.append(s)
            max_result_lenght = len(result[-1])
            for i, s in enumerate(result):
                s = " " * int((max_result_lenght - len(s)) / 2) + s + " " * int((max_result_lenght - len(s)) / 2)
                rows = (i + 2) // 10
                print(s + rows * '\n')
            break
        except Exception as ex:
            print(f"Ошибка {ex}")
