import math
idx_0_mkt_price = 100 # eth
idx_1_mkt_price = 1 # dai

def pool_info(pool):
    print("pair1",pool[0])
    print("pair2",pool[1])


def pool_market_value(pool):
    pool_mkt_value = (pool[0] * idx_0_mkt_price) + (pool[1] * idx_1_mkt_price)
    print("Pool market value",pool_mkt_value)
    return pool_mkt_value

def pool_constant_product(pool):
    constant_product = pool[0] * pool[1]
    return constant_product

def add_liquidity(qty1,qty2):
    print()
    return [pool[0] + qty1, pool[1] + qty2]

def print_liquidity(pool):
    idx_0_liquidity = math.sqrt(pool_constant_product(pool)/idx_0_mkt_price)
    idx_1_liquidity = math.sqrt(pool_constant_product(pool)*idx_0_mkt_price)
    return idx_0_liquidity,idx_1_liquidity

#ethdai
pool = [99,9900]

pool_info(pool)
pool_market_value(pool)
print(pool_constant_product(pool))
pool = add_liquidity(1,100)
pool_info(pool)
pool_market_value(pool)
pool_constant_product(pool)
print(print_liquidity(pool))