def main():
    n, x = map(int, input().split())  # xは必ずaの要素である
    a = list(map(int, input().split()))

    a.sort()

    i_left, i_right = 0, n
    i = (i_left + i_right) // 2

    while 0 < i < n:
        if x == a[i]:
            break
        if x > a[i]:
            i_left = i
        else:
            i_right = i
        i = (i_left + i_right) // 2

    print(i + 1)  # 問題の添字 = index + 1


if __name__ == "__main__":
    main()
