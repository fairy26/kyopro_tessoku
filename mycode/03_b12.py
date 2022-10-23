def f(x):
    return x**3 + x


def main():
    n = int(input())

    left, right = 1.0, 100.0
    for _ in range(20):  # なんで20回までで終わるん？
        mid = (left + right) / 2
        if n > f(mid):
            left = mid
        else:
            right = mid

    print(mid)


if __name__ == "__main__":
    main()
