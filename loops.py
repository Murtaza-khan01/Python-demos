i=100
while i<=1:
    print(i)
    i -= 1

n=int(input("enter your number:"))
j=1
while j<=10:   ####stopping condition
    print(n*j)
    j+=1      

heroes= ["ironman", "thor","superman","itachi"]

idex=0
while idex < len(heroes):
    print(heroes[idex])
    idex+=1

####using break keyword
z=1
while z<=5:
    print(z)
    if(z == 3):
        break
    z+=1

####continue keyword will skip 
f=1
while f<=10:
    if(f == 5):
        f+=1
        continue
    print(f)
    f+=1

u=1
while u>=6:
    print(u)
    if(u == 3):
       break
u+=1

t=1
while t>=10:
    if(t ==4):
        u+=1
        continue
    print(t)
    u+=1
######for loops for sequential traversing

list1=[1,4,9,16,25,36,49,64,81,100]
for val in list1:
    print(val)
 
tuple1=(1,4,16,25,36,49,64)
for num in tuple1:
    if(num == 4):
        print("4 is found")
        break
    print(num)

###range function using for loop
for i in range(20):
    print(i)