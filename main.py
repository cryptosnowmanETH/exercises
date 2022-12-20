"""for i in range(1,13):
    print(i)"""
    
numbers = list(range(1,13))

"""print(numbers[2:4])"""

"""print(numbers[::2])"""

"""print(numbers[::-1])"""

#create a new numbers list with every number in numbers to be squared 

#take each square it, append to a new list 

""""squareds = []
for number in numbers:
   squared = number**2
   squareds.append(squared)
print(squareds)"""

#list comprehension

"""squareds = [squared**2 for squared in numbers]
print(squareds)"""

#list called named 

"""names = ["Andy", "Andrew", "Jason", "Danny", "Glen"]
new_names = [name.upper() for name in names if name[0] == "A"]
print(new_names)"""

"""person = ["Fred", 41, "Green", 6.4]
print(person[3])"""

#key must be unique 
#hashing takes unique values and converts to another unique value. 
#when you hash a to b you can hash b to a 

person = {"name": "Fred", "age": 41, "favorite_color":"Green", "Weight": 6.4}
"""print(person["name"])"""

#change name value 
"""person["name"] = "Gary"
print(person["name"])"""

#create a new key value pair if a key doesn't exist 
person["telephone"] = "911"

#name: iterator. Converts dictionary to list of tuples when you iterate on it 
#unpacks the tuple into key and value 
"""for key, value in person.items():
    #printf converts all variables in double quotes into strings 
    #variable format strings 
    print(f"{key=} {value=}")

print(person.items())"""

#list of disctionaries 
#key becomes the value and the value is the dictionary 

people = {
    "Fred": {"age": 41, "favorite_color":"Green", "Weight": 6.4},
    "Gary": {"age": 32, "favorite_color":"blue", "Weight": 140},
    "Tom": {"age": 26, "favorite_color":"yellow", "Weight": 160},
}
print(people["Fred"]["age"])

colors = {
    "green": {"name": "fred", "age":41 }
}

#print fred
#print age
#print fav color
#print 
#gary 


#name is Fred, name detail is value of the key 
# in second for loop, key is the key inside second dictionary age in this case and value is the value of that key in name details which is the dictionary valiue associated with the fred key
for name, name_details in people.items():
    print(name)
    for key, value in name_details.items():
        print(key,value)
        
        
