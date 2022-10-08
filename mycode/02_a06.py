def main():
    n, q = map(int, input().split())
    arr = tuple(map(int, input().split()))

    total = [0]
    for i, num in enumerate(arr):
        total.append(total[i] + num)  # 前日までの合計+当日

    for _ in range(q):
        l, r = map(int, input().split())
        print(total[r] - total[l - 1])


if __name__ == "__main__":
    main()
