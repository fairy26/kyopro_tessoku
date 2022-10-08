def main():
    h, w = map(int, input().split())
    grid = [[] for _ in range(h)]
    for i in range(h):
        grid[i] = list(map(int, input().split()))

    total = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            value = grid[i - 1][j - 1]
            total[i][j] = value + total[i - 1][j] + total[i][j - 1] - total[i - 1][j - 1]

    q = int(input())
    for i in range(q):
        a, b, c, d = map(int, input().split())
        print(total[c][d] - total[a - 1][d] - total[c][b - 1] + total[a - 1][b - 1])


if __name__ == "__main__":
    main()
