def main():
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if 1 <= k - (i + j) <= n:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
