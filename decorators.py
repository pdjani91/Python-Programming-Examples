def decorators_function(any_function):
    def wrapper_function():
        print('This is awsome function')
        any_function()
    return wrapper_function

@decorators_function #this is sortcut and its decorators
def func1():
    print('this is function1')  
func1()

@decorators_function
def func2():
    print('this is function2')
func2()