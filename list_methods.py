list=[1,2,3,4,5]
print(list.append(6))
print(list)    ####to append an element at the end of the list

list1=["mubeen","aboha","mustafa"]
print(list1.insert(1,"mujtaba"))  ####to insert an element at   a specific index
print(list1)

list2=[10,20,30,40,50]
print(list2.remove(30))   ####to remove an element from the list        
print(list2)

list3=[100,200,300,400]
print(list3.pop())    ####to remove the last element from the list  
print(list3)

list4=[5,2,8,1,4]
print(list4.sort())   ####to sort the list in ascending order  
print(list4)

list5=[50,20,80,10,40]
print(list5.sort(reverse=True))   ####to sort the list in descending order
print(list5)    


list6=[1,2,3,4,5]
print(list6.reverse())   ####to reverse the list 
print(list6)    

list7=[10,20,30,20,50]
print(list7.count(20))    ####to count the occurrences of an element in the list
print(list7)    