def main():
    n, x = map(int, input().split())
    arr = tuple(map(int, input().split()))
    if x in arr:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
