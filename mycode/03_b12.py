def check(target, x):
    num = x**3 + x
    if target >= num:
        return True
    return False


def main():
    n = int(input())

    left, right = 1.0, float(n)
    while left < right:
        mid = round((left + right) / 2, 3)
        if check(n, mid):
            left = mid + 0.001
        else:
            right = mid - 0.001

    print(left)


if __name__ == "__main__":
    main()
