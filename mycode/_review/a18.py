# 復習日: 2022/11/30
# 結果: 何も見ずに解けた


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        card_num = A[i - 1]
        for j in range(S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= card_num:
                dp[i][j] = dp[i][j] or dp[i - 1][j - card_num]

    print("Yes") if dp[N][S] else print("No")


if __name__ == "__main__":
    main()
