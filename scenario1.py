from Uniswap import Pool

ethdai = Pool(('eth,dai'),[99,9900],100,1)
ethdai.info()
ethdai.add_liquidity(1,100)
ethdai.info()
ethdai.update_mkt_price(120,1)
ethdai.info()
