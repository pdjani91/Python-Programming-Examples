def decorators_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('This is awsome function')
        return any_function(*args,**kwargs)
    return wrapper_function

@decorators_function #this is sortcut and its decorators
def func1(a):
    print(f'this is function1 with argument {a}')  
func1(5)

@decorators_function
def add(a,b):
    return a+b
print(add(2,3))