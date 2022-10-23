from bisect import bisect_right


def main():
    N = int(input())
    A = list(map(int, input().split()))

    X = sorted(list(set(A)))
    B = []
    for i, a in enumerate(A):
        B.append(bisect_right(X, a))

    print(*B)


if __name__ == "__main__":
    main()
