#Similar to hash tables in other languages
#Time complexity of O(1)
#Unordered collection of data values
#Hold key:value pair

dict1 = {"name":"Miguel", "numbers":[1,2,3,4]}
print(dict1)

#To access an element using a key 
print(dict1["name"])
print(dict1["numbers"])

#Accesing an element using get() method
#Get works with indexes
print(dict1.get(0))