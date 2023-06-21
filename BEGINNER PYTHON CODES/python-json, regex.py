# the_json

import json
x= '{"name":"chandu","age":30,"city":"newyork"}'
y=json.loads(x)
print(y["age"])

# converting to json

import json
x ={
    "name":"chandu",
    "age":18,
    "city":"ongole"


}

# givig indentaion and ordering the result 
y =json.dumps(x,indent=4,sort_keys =True)
print(y)

# using seprataors
import json
x ={
    "name":"chandu",
    "age":18,
    "city":"ongole"

}
# using separators
y =json.dumps(x,indent=4,separators =(".","="))
print(y)











# python regex
# checking if the string starts with my and ends with chandana
import re
a = "my name is saichandana"
x = re.search("my.*chandana$",a)
print(x)


# using the regex function
# here we gonna use the special characters like\s \a etc
# the four different functions were findall , search , split , sub

# using the findall: returns all the matches that present in the string
import re
a = "mynameissai chandana"
x = re.findall("s",a)
print(x)

# using the search :  search the string for a match returns the
#match object if it matches

import re
a = " mynameissai chandana"
x = re.search("\s",a)#using the special character 
print(x)

# using the split: used to split the string
#we can mention the ocuurences by max parameter

import re
a = "my name is saichandana"
x=re.split("\s",a,1)# using the special character
print(x)

# using the sub function : it just replaces a particular character in the string
# we can mention the n.o replacements by using the count number
import re 
a = "my hari is hari chandana"
x = re.sub("hari","sai",a ,1)
print(x)











