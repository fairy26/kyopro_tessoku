# 復習日: 2022/11/20
# 結果: 方針1: 何も見ずに解けた, 方針2: 完全に忘れていた


def main():
    N, K = map(int, input().split())  # <=10**5, <=10**9
    A = list(map(int, input().split()))  # <=10**9 * N

    #     i |  0  1  2  3  4  5  6
    #     A | 11 12 16 22 27 28 31
    # <= 10 |  ^  o  o              |  2
    #       |     ^  o  o           |  2
    #       |        ^  o           |  1
    #       |           ^  o  o  o  |  3
    #       |              ^  o  o  |  2
    #       |                 ^  o  |  1
    #       +-----------------------+----
    #                               | 11 <- Answer

    # 方針1
    # each -> slice -> bisect
    # O(N)  *  O(k)  * O(logk)
    # いやsliceせずに添字で引き算したらO(NlogN)かな？
    from bisect import bisect_right

    ret = 0
    for i_a in range(N):
        i_in = bisect_right(A, A[i_a] + K) - 1
        ret += i_in - i_a

    print(ret)

    # 方針2: しゃくとり法
    ret = 0
    j = 0
    for i in range(N):
        while j < N and A[j] <= A[i] + K:
            j += 1
        ret += (j - 1) - i
    print(ret)


if __name__ == "__main__":
    main()
