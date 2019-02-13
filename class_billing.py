class Laptop:
    def __init__(self, brand, model_name, price):
        #Instance Varible Declaration
        self.brand = brand
        self.name = model_name
        self.price = price
        
    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

laptop1 = Laptop('Lenovo','G570',10000)

print(laptop1.apply_discount(10))