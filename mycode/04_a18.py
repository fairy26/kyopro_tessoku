"""
# 問題文
N 枚のカードが一列に並べられており、左から i 番目のカード（以下、カード i とする）には整数 A_i が書かれています。
カードの中からいくつかを選んで、書かれた整数の合計が S となるようにする方法は存在しますか。

# 制約
* 1≤N≤60
* 1≤S≤10000
* 1≤A_i≤10000
* 入力はすべて整数
"""


def _debug(dp, S):
    print("  |", *list(range(S + 1)))
    print("--+-" + "--" * (S + 1))
    for i, l in enumerate(dp):
        print(i, end=" | ")
        for ok in l:
            if ok:
                print("o", end=" ")
            else:
                print("x", end=" ")
        print()
    print()


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[False] * (S + 1) for _ in range(N + 1)]

    dp[0][0] = True
    for i in range(1, N + 1):  # O(N*S)
        for j in range(S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= A[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]
        # _debug(dp, S)

    print("Yes") if dp[N][S] else print("No")


if __name__ == "__main__":
    main()
