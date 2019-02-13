class Laptop:
    def __init__(self, brand, model_name, price):
        #Instance Varible Declaration
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + '' + model_name

#Object Declaration        
laptop1 = Laptop('Lenovo','G570',32850)

# print(laptop1.brand)
# print(laptop1.name)
# print(laptop1.price)

print(laptop1.laptop_name)