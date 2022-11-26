def main():
    N = int(input())
    P, A = [0] * (N + 1), [0] * (N + 1)
    for i in range(1, N + 1):
        P[i], A[i] = map(int, input().split())

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for block_len in reversed(range(0, N - 1)):
        for l in range(1, N + 1 - block_len):
            r = l + block_len

            score_r = A[r + 1] if r < N and l <= P[r + 1] <= r else 0
            score_l = A[l - 1] if l > 1 and l <= P[l - 1] <= r else 0

            if l == 1:
                dp[l][r] = dp[l][r + 1] + score_r  # 右端 r+1 を取り除く
                continue

            if r == N:
                dp[l][r] = dp[l - 1][r] + score_l  # 左端 l-1 を取り除く
                continue

            dp[l][r] = max(
                dp[l][r + 1] + score_r,  # 右端 r+1 を取り除く
                dp[l - 1][r] + score_l,  # 左端 l-1 を取り除く
            )

    # 出力
    print(max([dp[i][i] for i in range(1, N + 1)]))


if __name__ == "__main__":
    main()
