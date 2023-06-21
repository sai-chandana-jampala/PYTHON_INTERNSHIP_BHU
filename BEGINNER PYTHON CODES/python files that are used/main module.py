#  creating and importing module 
import sai
sai.greeting("Jonathan")

# when using the function from a module
# use the syntax : module name . function name
a =sai.person["a"]
print(a)
# you can even import with another name 
import sai as chandu
a= chandu.person["a"]
print(a)

# built in modules
import platform
x = platform.system()
print(x)

# using the dir function
import platform
x= dir(platform)
print(x)
 
# import only a certain part from the module 
from sai import person
print(person["a"])
