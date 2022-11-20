sample_in = """
5
2 4 1 3
5 3 7
"""

sample_out = """
8
"""

#  +-------5------+ +------7-------+
#  |              | |              |
# [0] -2- [2] -4- [5] -1- [5] -3- [8]
#          |               |
#          +-------3-------+


def main():
    N = int(input())  # [3, 10^5]
    A = list(map(int, input().split()))  # [1, 100] * (N-1)
    B = list(map(int, input().split()))  # [1, 100] * (N-2)

    rout = [0] * N

    for i in range(N):
        if i == 0:
            rout[i] = 0
        elif i == 1:
            rout[i] = A[i - 1]
        else:
            rout[i] = min(rout[i - 1] + A[i - 1], rout[i - 2] + B[i - 2])

    print(rout[-1])


if __name__ == "__main__":
    main()
