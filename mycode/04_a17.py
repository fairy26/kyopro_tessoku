sample_in = """
5
2 4 1 3
5 3 3
"""

sample_out = """
4
1 2 4 5
"""

#    +-----5-----+   +-----3-----+
#   /             \ /             \
# [0] -2- [2] -4- [5] -1- [5] -3- [8]
#           \             /
#            +-----3-----+
#
#  1 ----> 2 ------------> 4 ----> 5  |  K = 4
#  1 ------------> 3 ------------> 5  |  K = 3


sample_in_2 = """
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31
"""

sample_out_2 = """
7
1 2 4 5 6 8 10
"""


def main():
    N = int(input())  # [3, 10^5]
    A = list(map(int, input().split()))  # [1, 100] * (N-1)
    B = list(map(int, input().split()))  # [1, 100] * (N-2)

    # DPで探索
    route = [0] * N
    for i in range(N):
        if i == 0:
            route[i] = 0
        elif i == 1:
            route[i] = A[i - 1]
        else:
            route[i] = min(route[i - 1] + A[i - 1], route[i - 2] + B[i - 2])

    # 復元
    ans = [N]
    i = N - 1
    while i > 0:
        if route[i] == route[i - 1] + A[i - 1]:
            i -= 1
        else:
            i -= 2
        ans.append(i + 1)  # +1: idx -> num

    ans.reverse()

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
