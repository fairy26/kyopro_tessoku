def main():
    n = int(input())

    for i in list(range(9))[::-1]:
        wari = 1 << i  # 2のx乗
        print((n // wari) % 2, end="")


if __name__ == "__main__":
    main()
