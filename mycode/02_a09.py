def main():
    h, w, n = map(int, input().split())

    changes = [[0] * (w + 2) for _ in range(h + 2)]  # 降雪境界

    for _ in range(n):
        a, b, c, d = map(int, input().split())
        changes[a][b] += 1
        changes[a][d + 1] -= 1
        changes[c + 1][b] -= 1
        changes[c + 1][d + 1] += 1

    total = [[0] * (w + 1) for _ in range(h + 1)]  # 累積積雪量
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            total[i][j] = total[i][j - 1] + changes[i][j]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            total[i][j] += total[i - 1][j]

    for i in range(1, h + 1):
        print(*total[i][1:])


if __name__ == "__main__":
    main()
