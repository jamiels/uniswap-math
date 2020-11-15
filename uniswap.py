import math
class Pool:
    def __init__(self,names,seed_pool,mp1,mp2):
        self.names = names
        self.pool = seed_pool
        self.mp1 = mp1
        self.mp2 = mp2
        self.added1 = 0
        self.added2 = 0
        self.value_added = 0

    def market_value(self):
        pool_mkt_value = (self.pool[0] * self.mp1) + (self.pool[1] * self.mp2)
        return pool_mkt_value

    def constant_product(self):
        return self.pool[0] * self.pool[1]

    def add_liquidity(self,q1,q2,p1,p2):
        self.added1 = self.added1 + q1
        self.added2 = self.added2 + q2
        self.pool [0]= self.pool[0] + q1
        self.pool [1]= self.pool[1] + q2
        self.value_added = (q1 * p1) + (q2 * p2)
        print('Value added',self.value_added)

    def liquidity(self):
        cp = self.constant_product()
        idx_0_liquidity = math.sqrt(cp/self.mp1)
        idx_1_liquidity = math.sqrt(cp*self.mp1)
        return idx_0_liquidity,idx_1_liquidity

    def update_mkt_price(self,mp1,mp2):
        self.mp1 = mp1
        self.mp2 = mp2

    def liquidity_value(self):
        p1 = self.added1 / self.pool[0]
        p2 = self.added2 / self.pool[1]
        l1, l2 = self.liquidity()
        value = (p1*l1*self.mp1) + (p2 * l2 * self.mp2)
        return value

    def pl(self):
        return self.liquidity_value() - ((self.added1 * self.mp1) + (self.added2 * self.mp2))

    def info(self):
        print()
        print(self.names[0],self.pool[0],':',self.names[1],self.pool[1],'Market value:',self.market_value(),'Constant product:',self.constant_product())
        print('Liquidity:')
        l1, l2 = self.liquidity()
        print('\t',self.names[0],':',l1)
        print('\t',self.names[1],':',l2)
        print("Pool market value: $",self.market_value())
        print('LPs value:', self.liquidity_value())
        print('PL: ',self.pl())