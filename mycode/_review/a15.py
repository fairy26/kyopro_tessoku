# 復習日: 2022/11/20
# 結果: 何も見ずに解けた

sample_in = """
5
46 80 11 77 46
"""

sample_out = """
2 4 1 3 2
"""

sample_in_00 = """
87
50 77 40 31 5 57 90 16 24 96 41 5 67 76 47 56 17 66 35 35 35 22 8 67 65 29 64 8 61 19 53 18 7 43 22 79 13 98 90 58 1 75 17 74 97 97 27 21 81 23 51 66 60 98 87 13 47 72 23 10 2 89 61 29 76 35 99 76 36 73 78 76 41 26 9 81 96 11 13 85 32 12 78 79 15 33 48
"""

sample_out_00 = """
33 50 28 23 3 37 57 12 19 58 29 3 44 49 31 36 13 43 26 26 26 17 5 44 42 22 41 5 40 15 35 14 4 30 17 52 10 60 57 38 1 48 13 47 59 59 21 16 53 18 34 43 39 60 55 10 31 45 18 7 2 56 40 22 49 26 61 49 27 46 51 49 29 20 6 53 58 8 10 54 24 9 51 52 11 25 32
"""

## run following code to check
# print(all[list(map(int, sample_out_00.split()))[i] == num for i, num in enumerate(ret)]))


def main():
    N = int(input())  # 10^5
    A = list(map(int, input().split()))  # 10^9

    from bisect import bisect_right

    A_ = sorted(list(set(A)))  # O(log(N)) + O(N)
    ret = []
    for a in A:  # O(N) * O(log(N))
        ret.append(bisect_right(A_, a))

    print(*ret)


if __name__ == "__main__":
    main()
