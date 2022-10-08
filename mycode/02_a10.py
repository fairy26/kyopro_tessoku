inputs = """\
7
1 2 5 5 2 3 1
2
3 5
4 6
"""


def main():
    n = int(input())  # 7
    a = list(map(int, input().split()))  # [1, 2, 5, 5, 2, 3, 1]
    d = int(input())  # 2
    max_left = [0] + a[:]
    max_right = a[:] + [0]
    for i in range(1, n + 1):
        max_left[i] = max(max_left[i - 1], a[i - 1])
        max_right[-1 - i] = max(max_right[-i], a[-i])
    # max_left  = [0, 1, 2, 5, 5, 5, 5, 5] (idx: _, 1, 2, 3, 4, 5, 6, 7 に対応)
    # max_right = [5, 5, 5, 5, 3, 3, 1, 0] (idx: 1, 2, 3, 4, 5, 6, 7, _ に対応)

    for _ in range(d):
        l, r = map(int, input().split())  # (3, 5), (4, 6)
        print(max(max_left[l - 1], max_right[r]))


if __name__ == "__main__":
    main()
