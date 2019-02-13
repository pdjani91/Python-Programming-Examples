user = {}

name = input("Enter your name : ")
age = input("Enter your age : ")
fav_movies = input("Enter your fav movies using seperated comma : ").split(',')
fav_songs = input("Enter your fav songs using seperated comma : ").split(',')

user ['name'] = name
user ['age'] = age
user ['fav_movies'] = fav_movies
user ['fav_songs'] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")