# 復習日: 2022/10/23
# 結果: 何も見ずに解けた


def main():
    D = int(input())
    N = int(input())
    L, R = [], []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    nums_attendance = [0] * (D + 1)  # NOTE: サイズで一度ミスった
    for i in range(N):
        nums_attendance[L[i] - 1] += 1
        nums_attendance[R[i]] -= 1

    total = 0
    for i in range(D):
        total += nums_attendance[i]
        print(total)


if __name__ == "__main__":
    main()
