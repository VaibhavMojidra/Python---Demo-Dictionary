#Dictionaries

d={}
print(type(d))

scrores={"vaibhav":99,"shreyas":98,"rohan":89}
print(scrores)

print(scrores["vaibhav"])
#print(scrores["Vaibhav"]) #throws KeyError: 'Vaibhav'
print("vaibhav" in scrores)
scrores["vaibhavi"]=35

print(scrores)

scrores["vaibhav"]=100 #overwrites

print(scrores)

del scrores["vaibhavi"] #deletes

print(scrores)

#Iterating over dictionaries

#method 1
for n in scrores:
    print(n) #n will be only key
    print(n+" "+str(scrores[n])) # using key you can access value


#method 2
for n,s in scrores.items():
    print(n+" "+str(s))


#Get all keys of dictionary
print(scrores.keys())

#Get all values of dictionary
print(scrores.values())

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

print(wardrobe)


