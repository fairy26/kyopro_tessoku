def main():
    d = int(input())
    n = int(input())
    total = [0] * d
    for _ in range(n):
        l, r = map(int, input().split())
        for i in range(l, r + 1):
            idx = i - 1
            total[idx] += 1

    for num in total:
        print(num)


if __name__ == "__main__":
    main()
