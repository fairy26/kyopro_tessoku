def check(target, arr, k):
    sum_num = sum(target // num for num in arr)

    if sum_num >= k:
        return True
    return False


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left, right = 0, 10**9

    while left < right:
        i = (left + right) // 2
        if check(i, a, k):
            right = i
        else:
            left = i + 1

    print(left)


if __name__ == "__main__":
    main()
