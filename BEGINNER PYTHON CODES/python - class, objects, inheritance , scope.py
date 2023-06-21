
# creating a class with its function
class sai:
    def __init__(a,name,age):
        a. name = name
        a. age = age
p1 = sai("chandana",19)
print(p1.name)
print(p1.age)
    
# function inside function
class sai:
    def __init__(a,name,age):
        a.name = name
        a.age = age
    def myfunc(a):
     print("my name is"+" "+ a.name)
p1 = sai("chandana",19)
p1.myfunc()
    
# modify object properties
class sai:
    def __init__(a,name,age):
        a.name = name
        a.age = age
    def myfunc(a):
     print("my name is"+" "+ a.name)
p1 = sai("chandana",19)
p1.age = 20
print(p1.age)

# delete object properties
class sai:
    def __init__(a,name,age):
        a.name = name
        a.age = age
    def myfunc(a):
     print("my name is"+" "+ a.name)
p1 = sai("chandana",19)
#del p1.name
#print(p1.name)

# deleting objects
class sai:
    def __init__(a,name,age):
        a.name = name
        a.age = age
    def myfunc(a):
     print("my name is"+" "+ a.name)
p1 = sai("chandana",19)
#del p1
#print(p1)

# when you just want to keep the empty class , you can use the pass statment 











# inheritance 

# creating a parent class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname , self.lastname)
x = person("sai", "chandana")
x.printname()
 
# adding the child class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname , self.lastname)
    class mystudent(person):
        pass
x = person("sai", "chandana")
x.printname()

# creating a child class with init function and adding paarmerers
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("sai", "chandana", 2055)
x.welcome()



# scope is nothing but the  global scope(global variable) and local scope(local variable)
