from abc import ABCMeta, abstractmethod


# Command Class
class Order(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


# Concrete Command Class 1
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# Concrete Command Class 2
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver
class StockTrade:
    def buy(self):
        print("you will buy stocks")

    def sell(self):
        print("you will sell stocks")


# Invoker
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


# Client
if __name__ == "__main__":
    # Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Agent
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)

