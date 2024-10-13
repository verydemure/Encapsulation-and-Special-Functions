class computer:

    def __init__(self):
        self.__maxprice = 900

    def printprice(self):
        print(f"Selling price:{self.__maxprice}")

    def setMaxprice(self,price):
        self.__maxprice = price

c = computer()
c.printprice()

c.__maxprice = 1000
c.printprice()

c.setMaxprice(1000)
c.printprice()