from functools import wraps

def print_function_data(function):
    def wrapper(*args,**kwargs):
        print(f"You are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper

@print_function_data
def addition(a,b):
    '''This is function takes two numbers as arguments and return thier sum'''
    return a+b

print(addition(10,15))