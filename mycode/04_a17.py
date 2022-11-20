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

    rout = [[0] * N for _ in range(2)]
    # rout[0][i]: cost
    # rout[1][i]: from i room

    rout[0][0] = 0
    rout[1][0] = None
    rout[0][1] = A[0]
    rout[1][1] = 0
    for i in range(2, N):
        costs = [rout[0][i - 1] + A[i - 1], rout[0][i - 2] + B[i - 2]]

        rout[0][i] = min(costs)
        rout[1][i] = i - (1 + costs.index(rout[0][i]))

    ans = [N]
    step = rout[1][-1]
    while step is not None:
        ans.append(step + 1)
        step = rout[1][step]

    ans.reverse()

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
