class Product():

    def __init__(self,no,name,price,count):
        self.no = no
        self.name = name
        self.price = price
        self.count = count


    def total_price(self):
        self.total = self.price*self.count

    def __str__(self):
        return f"{self.no},{self.name},{self.price},{self.count},{self.total}"
        