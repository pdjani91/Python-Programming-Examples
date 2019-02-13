#instance method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Parth' , 'Jani' , 27)
p2 = Person('Rahul' , 'Joshi' , 31)

print (p1.full_name())
print(p1.is_above_18())
#==========================================
l=[1,2,3]
l.append(4)
#actual list.append(l,4)
print (l)
#========================================
# l.clear
# actual list.clear(l)
# print(l)
#========================================
