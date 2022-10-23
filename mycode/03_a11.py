def main():
    n, x = map(int, input().split())  # xは必ずaの要素である
    a = list(map(int, input().split()))

    a.sort()

    i_left, i_right = 0, n

    while i_left <= i_right:
        i = (i_left + i_right) // 2

        if x == a[i]:
            break
        if x > a[i]:
            i_left = i + 1
        else:
            i_right = i - 1

    print(i + 1)  # 問題の添字 = index + 1


if __name__ == "__main__":
    main()
