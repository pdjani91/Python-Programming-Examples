class Person:
    def __init__(self, first_name, last_name, age):
        #Instance Varible Declaration
        print('init method // constructor get called')
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

#Object Declaration
p1 = Person('Parth', 'Jani', 27)
p2 = Person('Ankur', 'Trivedi', 30)

print(p1.person_first_name)
print(p2.person_first_name)
        