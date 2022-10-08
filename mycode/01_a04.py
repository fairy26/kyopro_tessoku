def main():
    n = int(input())

    n_digit = list("0000000000")
    i = len(n_digit) - 1

    if n != 0:
        while n > 1:
            n_digit[i] = str(n % 2)
            n //= 2
            i -= 1
        n_digit[i] = "1"

    print(*n_digit, sep="")


if __name__ == "__main__":
    main()
