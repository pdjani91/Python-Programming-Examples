# function retuning function
# def outer_func():
#     def inner_func():
#         print('Inside inner func')
#     return inner_func
# def outer_func2(msg):
#     def inner_func2():
#         print(f"Message is {msg}")
#     return inner_func2
# var = outer_func2 ("Hello there !")
# var()
# =============================================

#Function returning function (Closure) pratice (Function in Function)
def to_power(x): #x=3
    def calc_power(n): #n=2
        return n**x
    return calc_power
cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))

print (sum.__doc__)