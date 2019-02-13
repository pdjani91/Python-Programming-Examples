from functools import wraps

def decorators_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """This is wrapper function"""
        print('This is awsome function')
        return any_function(*args,**kwargs)
    return wrapper_function

@decorators_function
def add(a,b):
    '''This is add function'''
    return a+b

print(add.__doc__)
print(add.__name__)