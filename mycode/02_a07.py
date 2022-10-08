def main():
    d = int(input())
    n = int(input())
    changes = [0] * (d + 1)
    for _ in range(n):
        l, r = map(int, input().split())  # l日~r日 → l日: +1, r+1日: -1
        changes[l - 1] += 1
        changes[r] -= 1

    total = 0
    for i in range(d):
        total += changes[i]
        print(total)


if __name__ == "__main__":
    main()
