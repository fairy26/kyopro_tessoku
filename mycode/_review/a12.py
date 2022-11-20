# 復習日: 2022/11/20
# 結果: ロジックは思い出せたけど、具体的な二分探索の実装は方針を読んだ


def f(A: list[int], time: int):  # list[]のtype hintingはAtCoderでは使えないので注意
    return sum([time // a for a in A])


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    i_left, i_right = 0, 10**9
    while i_left < i_right:
        mid = (i_left + i_right) // 2
        num_printed = f(A, mid)
        if num_printed >= K:
            i_right = mid
        else:
            i_left = mid + 1

    print(i_left)


if __name__ == "__main__":
    main()
