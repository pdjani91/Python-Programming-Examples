# Any and All Function

def my_sum(*args):

    if all([type(i)==int or type(i)==float for i in args]):
        total = 0   
        for num in args:
            total += num
        return total
    else:
        return "Wrong Input"

print (my_sum(1,2,3,4,5,8.9,9.0))