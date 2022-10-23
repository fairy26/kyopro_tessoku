# 復習日: 2022/10/23
# 結果: 何も見ずに解けた


def main():
    H, W, N = map(int, input().split())
    GRID = [[0] * (W + 1) for _ in range(H + 1)]
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        GRID[a - 1][b - 1] += 1
        GRID[a - 1][d] -= 1
        GRID[c][b - 1] -= 1
        GRID[c][d] += 1

    for h in range(H):
        for w in range(W):
            GRID[h][w + 1] += GRID[h][w]

    for h in range(H):
        for w in range(W):
            GRID[h + 1][w] += GRID[h][w]

    for h in range(H):
        for w in range(W):
            print(GRID[h][w], end=" ")
        print()


if __name__ == "__main__":
    main()
