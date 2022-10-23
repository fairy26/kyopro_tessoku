from bisect import bisect_right


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i, num in enumerate(a):
        ans += bisect_right(a, num + k) - i - 1  # range - num自身; 「k以下」→ rightで含むように

    print(ans)


if __name__ == "__main__":
    main()
