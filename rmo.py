class Phone: #Base Class or Parent Class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"Calling {number}...."

class Smartphone(Phone): #Drived or Child Class, here Phone class is inherit to Smartphone class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):       # Phone.__init__(self,brand,model_name,price) #uncomman way

        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera

phone = Phone('Asus','Zenphone Max Pro M1',12999)
smartphone = Smartphone('OnePlus','5T',32999,'6 GB','64 GB','20 MP')
oneplus = FlagshipPhone('OnePlus','5T',32999,'6 GB','64 GB','20 MP','16 MP')

# print(phone.full_name())
# print(smartphone.full_name() + f"and price is {smartphone._price}")

print(smartphone.full_name())

print(help(Smartphone)) #MRO (Method Resolution Order)