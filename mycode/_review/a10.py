# 復習日: 2022/10/23
# 結果: 何も見ずに解けたけど、思い出す・添字の扱いに少し苦戦


def main():
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())
    L, R = [], []
    for _ in range(D):
        l, r = map(int, input().split())
        # 添字にして格納する
        L.append(l - 1)
        R.append(r - 1)

    max_l = [A[0]] * N
    max_r = [A[-1]] * N

    for i in range(1, N):
        max_l[i] = max(A[i], max_l[i - 1])
        max_r[-(i + 1)] = max(A[-(i + 1)], max_r[-i])

    for i in range(D):
        print(max(max_l[L[i] - 1], max_r[R[i] + 1]))


if __name__ == "__main__":
    main()
