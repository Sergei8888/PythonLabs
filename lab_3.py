def main():
    x = int(input("Введите число X: "))
    answer = []
    for c in range(0, 100):
        for b in range(0, 100):
            for a in range(0, 100):
                t = 3 ** a * 5 ** b * 7 ** c
                if t <= x:
                    answer += [t]
                else:
                    break
    print("Числа: ", *sorted(answer))


if __name__ == "__main__":
    main()
