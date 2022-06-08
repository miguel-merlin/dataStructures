#Data Structures (Lists)

#Lists are ordered collections of data
list1 = [1,2,3,"jello",2.3]
print(list1)

#It is costly efficiency wise to insert or delete elements at the beggining of lists, because all elements must be shifted. 
#The elements of a list can be accesed with an index

list2 = ["Hello", "World","Book",40.3,2]
print(list2[3])
print(list2[2])

#You can also acces elements of a list using negative indexes
print(list2[-1])
print(list2[-3])

#You can assign the value of an index to a variable
a = list2[3]
print(a)