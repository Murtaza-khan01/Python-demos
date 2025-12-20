movie1 = input("enter your first favorite movie name:")
movie2 = input ("enter your second favorite movie name:")
movie3 =input ("enter your third favorite movie name:")
movies=[movie1, movie2,movie3]
print(movies)

print(type(movies))


tuple1=(1,2,3,4,5)
print(tuple1)
print(type(tuple1))
print(tuple1[2])  ###accessing tuple elements
print(len(tuple1))  ###length of tuple  
###tuple with different data types
tuple2=("mubeen",12,90.5)      
print(tuple2)

###slicing of tuples
tuple3=(10,20,30,40,50)
print(tuple3[1:4])