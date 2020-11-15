import math
class Pool:
    def __init__(self,names,seed_pool,mp1,mp2):
        self.names = names
        self.pool = seed_pool
        self.mp1 = mp1
        self.mp2 = mp2

    def market_value(self):
        pool_mkt_value = (self.pool[0] * self.mp1) + (self.pool[1] * self.mp2)
        print("Pool market value: $",pool_mkt_value)
        return pool_mkt_value

    def constant_product(self):
        return self.pool[0] * self.pool[1]

    def add_liquidity(self,q1,q2):
        self.pool [0]= self.pool[0] + q1
        self.pool [1]= self.pool[1] + q2

    def liquidity(self):
        cp = self.constant_product()
        idx_0_liquidity = math.sqrt(cp/self.mp1)
        idx_1_liquidity = math.sqrt(cp*self.mp2)
        return idx_0_liquidity,idx_1_liquidity

    def update_mkt_price(self,mp1,mp2):
        self.mp1 = mp1
        self.mp2 = mp2

    def info(self):
        print()
        print(self.names[0],self.pool[0],':',self.names[1],self.pool[1],'Market value:',self.market_value(),'Constant product:',self.constant_product())
        print('Liquidity:')
        l1, l2 = self.liquidity()
        print('\t',self.names[0],':',l1)
        print('\t',self.names[1],':',l2)
        print()