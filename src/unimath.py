import math

eth = 10 ** 18
q96 = 2 ** 96
amount_eth = 1 * eth
amount_usdc = 5000 * eth


def price_to_tick(p):
    return math.floor(math.log(p, 1.0001))


def price_to_sqrtp(p):
    return int(math.sqrt(p) * q96)


def liquidity0(amount, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return (amount * (pa * pb) / q96) / (pb - pa)


def liquidity1(amount, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return (amount * q96) / (pb - pa)


def cal_amount0(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return int(liq * q96 * (pb - pa) / pa / pb)


def cal_amount1(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return int(liq * (pb - pa) / q96)


sqrtp_low = price_to_sqrtp(4545)
sqrtp_cur = price_to_sqrtp(5000)
sqrtp_upp = price_to_sqrtp(5500)

liq0 = liquidity0(amount_eth, sqrtp_cur, sqrtp_upp)
liq1 = liquidity1(amount_usdc, sqrtp_cur, sqrtp_low)

liq = int(min(liq0, liq1))

amount0 = cal_amount0(liq, sqrtp_upp, sqrtp_cur)
amount1 = cal_amount1(liq, sqrtp_low, sqrtp_cur)

print(amount0, amount1)
# Swap ETH for USDC
amount_in = 0.01337 * eth

print(f"\nSelling {amount_in/eth} ETH")

price_next = int((liq * q96 * sqrtp_cur) // (liq * q96 + amount_in * sqrtp_cur))

print("New price:", (price_next / q96) ** 2)
print("New sqrtP:", price_next)
print("New tick:", price_to_tick((price_next / q96) ** 2))

amount_in = cal_amount0(liq, price_next, sqrtp_cur)
amount_out = cal_amount1(liq, price_next, sqrtp_cur)

print("ETH in:", amount_in / eth)
print("USDC out:", amount_out / eth)



# price_low = 0.287
# price_current = 1.15
# price_high = 2.018
#
# amount_base = 1000 * eth
# amount_usdt = 2352 * eth
#
# sqrtp_low = price_to_sqrtp(price_low)
# sqrtp_cur = price_to_sqrtp(price_current)
# sqrtp_upp = price_to_sqrtp(price_high)
#
# liq0 = liquidity0(amount_base, sqrtp_cur, sqrtp_upp)
# liq1 = liquidity1(amount_usdt, sqrtp_cur, sqrtp_low)
#
# liq = int(min(liq0, liq1))
#
# amount0 = cal_amount0(liq, sqrtp_upp, sqrtp_cur)
# amount1 = cal_amount1(liq, sqrtp_low, sqrtp_cur)
#
# print(liq, amount0, amount1)
#
# price_next = 0.29
# sqrtp_next = price_to_sqrtp(price_next)
#
# amount_in = cal_amount0(liq, sqrtp_next, sqrtp_cur)
# amount_out = cal_amount1(liq, sqrtp_next, sqrtp_cur)
#
# print("arb in: ", amount_in / eth)
# print("usdc out: ", amount_out / eth)