str1="mubeen khan"    ##slicing for negative indexing
print(str1[-3:-1])

##endwith function
str2="i am coder"
print(str2.endswith("we"))

##capitalize func
str3="my name is mubeen"
print(str3.capitalize())

##replace func
str4="apna college"
print(str4.replace("apna","mera"))
###find word func

str5="we are learning python from apna college"
print(str5.find("are"))

##count fun for string

str6="we are learning python from apna college"
print(str6.count("are"))




str7="my name ia mubeen"
print(str7[-3:-2])
str9= "i am star"
print(str9.count("am"))


a=input("first name:")
print(len(a))

str10="my $name is mibeen$"
print(str10.count("$"))


light=input("light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go") 
else:
    print("light is broken")      