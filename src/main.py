from utils import *


def estimate_y_amount(p, a, b, x):
    print(f"Example 1: how much of USDC I need when providing {x} ETH at this price and range?")
    sp = p ** 0.5
    sa = a ** 0.5
    sb = b ** 0.5
    L = get_liquidity_0(x, sp, sb)
    y = calculate_y(L, sp, sa, sb)
    print("amount of USDC y={:.2f}".format(y))


def main():
    estimate_y_amount(1.1426, 0.2843, 1.9984, 1000)


main()
