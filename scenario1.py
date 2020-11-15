from Uniswap import Pool


# based on https://pintail.medium.com/uniswap-a-good-deal-for-liquidity-providers-104c0b6816f2

ethdai = Pool(('eth,dai'),[99,9900],100,1)
ethdai.info()
ethdai.add_liquidity(1,100,100,1)
ethdai.info()
ethdai.update_mkt_price(120,1)
ethdai.info()


#todo

# calc price_ratio
# calc divergence
# graph
