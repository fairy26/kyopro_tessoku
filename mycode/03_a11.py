from bisect import bisect_right


def main():
    n, x = map(int, input().split())  # xは必ずaの要素である
    a = list(map(int, input().split()))

    print(bisect_right(sorted(a), x))


if __name__ == "__main__":
    main()
