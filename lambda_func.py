# Define a function take any number of list containg number
#[1,2,3],[4,5,6],[7,8,9]
# Return avarage
#(1+4+7)/3,(2+5+8)/3,(3+6+9)/3
#==================================================
# def avarage_finder(*args):
#     avarage = []
#     for i in zip(*args):
#         avarage.append(sum(i)/len(i))
#     return avarage
# print(avarage_finder([1,2,3],[4,5,6],[7,8,9]))
#Output : [4.0, 5.0, 6.0]
#====================================================

#Above code written with lambda function in one line
avarage_finder = lambda *args: [sum(i)/len(i) for i in zip(*args)]
print(avarage_finder([1,2,3],[4,5,6],[7,8,9]))
#====================================================