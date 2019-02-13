# square =[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# square = [i**2 for i in range(1,11)] #list comprehension
# print(square)

names = ['Parth','Ankur','Jeet']
# new_list = []
# for i in names:
#     new_list.append(i[0])
# print(new_list)

new_list = [i[0] for i in names] #list comprehension
print(new_list)