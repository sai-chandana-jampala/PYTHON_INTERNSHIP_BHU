# list 
# accesing the list 
sai = [ 1 , 2 ,3 ]
print(sai[0])
print(sai[0:1])
print(sai[-2:-1])

if 1 in sai:
    print("yes its present")
else:
    print("not present")

#change list items
sai = ["a","b","c"]
sai[0] = "d"
print(sai)
sai[1:3]="e","f"
print(sai)
sai.insert(3 , "g") # changing
print(sai)

# adding
sai = [1, 2 ,3]
sai.append(4)   # appending
print(sai)
chandana = [5, 6 , 7]
sai.extend(chandana)  # extending
print(sai)

# substractig
sai = [1,2,3]
sai .remove(3) # removing
print(sai)
sai.pop(1) # pop method
print(sai)
sai.clear() # clearing
print(sai)

# using loops
sai = [ "1","2","3"]
for x in sai:
    print("\n",x)
"\n"
for i in range(len(sai)):
    print("\n",sai[i])
sai = [ "1","2","3"]
x = 0
"\n"
while x <len(sai):
    print("\n",sai[x])
    x = x +1
         

# list comprehension
sai = [1,2,3]
[print(x) for x in sai]
newlist = [ x for x in range(10) if x<5]   #printing 10 elements 
print(newlist)


# sorting
x = ["c","b","a"]
x.sort()        
print(x)
x = ["c","b","a"]
x.sort(reverse = True) #descending order
print(x)
x = ["c","b","a"]
x.sort(key = str.lower)   #case sensitive
print(x)
x = ["c","b","a"]
x.reverse()   # reversing irrespective of alphabetic order
print(x)

# copy lists
x = [1,2,3]
y=x.copy()
print(y)
x = [1,2,3]
y = list(x)  # using list method
print(y)






# tuple

a = ( 1,2,3 )
b = ("a",)
print(type(b))

# accesing the tuple
a = (1,2,3)
print(a[0])
# aceesing the tuple is the same as accesing the list

# updating elements in python - you cant add or remove elemnts in python
# we can do it by converting it to  list
a = (1,2,3)
b = list(a)
b[0] = 4
c = tuple(b)
print(c)
# in the same way by converting it to list we can add and remove elements

#unpack tuples
a = ( 1,2,3)
(d,b,c)=a
print(d)
# usage of asetrisk
fruits = ("banana","mango","apple", "pinapple")
(a,*b,c)=fruits
print(b)

# looping through the tuples is same as the list

# python joint tuples
a = ("a","b","c")
b = ("d","e","f")
c = a+b
print(c)
# multiply the tuples
c = ("d","e","f")
d = c*2
print(d)



# set

a = { a,b,c}

# acessing a set
# since its uniindexed you cant access it through index numbers
# you can acess it by using the for loop
for x in a:
   print (x)

# to check if some item is present
a = {"a","b","c"}
if ("b" in a):
   print("yes")
else:
   print("no")

#add items
   # to add one item we can simply use the add method
   # to add a list ot some other , we can use the update method
a = {1,2,3}
a.add(4)
print(a)
b = {5,6,7}
a.update(b)
print(a)

# remove itsems
  # to remove items in the set we can use discard or remove or pop
  # we can also use del or clear
a = {1,2,3}
a.remove(2)
print(a)
a = {1,2,3}
a.discard(1)
print(a)
a = {1,2,3}
a.pop()
print(a)
a = {1,2,3}
a.clear()
print(a)
#a = {1,2,3}
#del a # this will shows an error bcz we deleted 
#print(a)

# join sets
# to add the sets we can use the union method or update method  (: this 2 mthods will remove the duplcates)
#to keep only duplicate elements we need to use x. intersection(y)
# to keep the remaining numbers with out duplicates (x. symmetric_difference(y)
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
a = {1,2,3}
b = {3,4,5} 
print(a. intersection(b))
a = {1,2,3}
b = {3,4,5}
print(a. symmetric_difference(b))








# dictionaries
sai ={
    "ramana":"police",
    "sreelakshmi":"teacher",
    "harika":4
    }

# aceesing dict items
# you can acess dict items by using the get and using its key name
x = print(sai["harika"])
x = print(sai.get("harika"))
x = print (sai.keys())
x = print (sai.values())
x = print(sai.items())

# you  can change and add the dictionarie items
sai ={
    "ramana":"police",
    "sreelakshmi":"teacher",
    "harika":4
    }
sai["ramana"]= 5
print(sai.values())
sai["chandana"]=1
print (sai.items())

# deleteing the items
sai ={
    "ramana":"police",
    "sreelakshmi":"teacher",
    "harika":4
    }
sai.pop("harika")
print(sai)
del sai["ramana"]
print(sai)
sai.clear()
print(sai)

# python loop dictionaries
sai ={
    "ramana":"police",
    "sreelakshmi":"teacher",
    "harika":4
    }
for x in sai.keys():
    print(x)
for x in sai.values():
    print(x)
for x in sai.items():
    print(x)

# pytho copy dictionaries
sai ={
    "ramana":"police",
    "sreelakshmi":"teacher",
    "harika":4
    }
harika = sai.copy()
print(harika)
harika = dict(sai)
print(harika)

# python - nested dictionaries
child1={
    "name":"sai",
    "age":36
    }
child2={
    "name":"harika",
    "age":22
    }

parents={
     "first" : child1,
     "second" : child2
    }
print(parents)
    
