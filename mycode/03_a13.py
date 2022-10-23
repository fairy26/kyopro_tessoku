def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(n - 1):

        if i == 0:
            right = 0

        for j in range(right + 1, n):  # [前回超えたところ, n-1]
            if a[j] > a[i] + k:  # 差がkを超えたら
                j -= 1  # 超える1つ前まで添字を戻して
                break

        ans += j - i
        right = j

    print(ans)


if __name__ == "__main__":
    main()
