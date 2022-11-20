# 復習日: 2022/11/20
# 結果: 惜敗; 探索するi_の動き、探索回数の20、それぞれがまだ理解できていない


def f(x):
    return x**3 + x


def main():
    N = int(input())  # 1 <= N <= 10**5

    # x  =>  x**3+x <=10**5?
    # ------------------------
    # 10 =>   1,010 True
    # 20 =>   8,020 True
    # 30 =>  27,030 True
    # 40 =>  64,040 True
    # 50 => 125,050 False
    #
    # 0 < 解 < 50
    # ^i_left   ^i_right

    i_left, i_right = 0.0, 50.0
    for _ in range(20):
        i_mid = (i_left + i_right) / 2

        if f(i_mid) > N:
            i_right = i_mid
        else:
            i_left = i_mid

    print(i_left)


if __name__ == "__main__":
    main()
