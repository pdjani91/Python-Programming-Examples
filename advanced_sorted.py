mobile =    [
    {'model':'Asus Zenphone Max Pro M1','price':12999},
    {'model':'One Plus 5T','price':34999},
    {'model':'Xiomi Note 5 Pro','price':14999},
    {'model':'Samsung Note 9','price':59999}
]

sorted_mobile = sorted(mobile,key = lambda i : i['price'],reverse = True)

print(sorted_mobile)