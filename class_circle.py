class Circle:
    pi = 3.14 #CLASS VARIABLE
    def __init__(self,radius):
        self.radius = radius

    def calc_ciecumference(self):
        return 2*Circle.pi*self.radius # 2 x class_name.class_variable x self.instance_variable

c = Circle(4)
print(c.calc_ciecumference())