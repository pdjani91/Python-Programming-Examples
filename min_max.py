student  = [
    {'name':'Parth','score':90,'age':27},
    {'name':'Ankur','score':80,'age':30},
    {'name':'Ankit','score':70,'age':29}
]
print(max(student,key=lambda item:item.get('age'))['name'])

student = {
    'Parth' : {'score':90,'age':27},
    'Ankur' : {'score':60,'age':30},
    'Karan' : {'score':70,'age':29},
}
print(min(student,key = lambda item : student[item]['age']))