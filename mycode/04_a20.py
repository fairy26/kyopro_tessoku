"""ex.
T = "tokyo"
S = "kyoto"

T\S|   | k | y | o | t | o |
 - + - + - + - + - + - + - +
   | 0 | 0 | 0 | 0 | 0 | 0 |
 - + - + - + - + - \ - + - +
 t | 0 | 0 | 0 | 0 | 1 | 1 |
 - + - + - + - \ - + - \ - +
 o | 0 | 0 | 0 | 1 | 1 | 2 |
 - + - \ - + - + - + - + - +
 k | 0 | 1 | 1 | 1 | 1 | 2 |
 - + - + - \ - + - + - + - +
 y | 0 | 1 | 2 | 2 | 2 | 2 |
 - + - + - + - \ - + - \ - +
 o | 0 | 1 | 2 | 3 | 3 | 3 |
 - + - + - + - + - + - + - +
"""


def main():
    S = input()
    T = input()
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[len(S)][len(T)])


if __name__ == "__main__":
    main()
