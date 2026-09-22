from product import*
from products import*

product = Products()

p1 = Product(1,"사과",1000,3)
p2 = Product(2,"바나나",2000,2)

product.add(p1)
product.add(p2)

p1.total_price()
p2.total_price()

product.print()