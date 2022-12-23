from collections import defaultdict 

#https://pynative.com/python-dictionary-exercise-with-solutions/
#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

"""sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}"""

#new_dict = {}
#new_dict['name'] = ['kelly']
#new_dict['salary'] = ['8000']

#print(new_dict)

#new_dict.get(name)



#expected output 
#{'name': 'Kelly', 'salary': 8000}

#https://www.my-courses.net/p/python-dictionary-exercises.html

#Write a Python program that combines by concatenating these three dictionaries into one.

dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
dicTablet = {"Sumsung": 15, "Other": 13}

#automatically making the value associated with the key an empty list 
dd = defaultdict(int)

for d in [dicPC, dicPhone, dicTablet]:
    for key, value in d.items(): 
        dd[key] += value
        #value with [] is 
#print(dd)

"""dd = defaultdict(list)

for d in [dicPC, dicPhone, dicTablet]:
    for key, value in d.items(): 
        dd[key].append(value)
       
print(dd)"""

"""d4 = {} 
d4.update(dicPC)
d4.update(dicPhone)
d4.update(dicTablet)"""
#print(d4)

"""for key, value in [dicPC, dicTablet, dicPhone]:
    d4 = {}
    if key == key: 
        d4['key'] = value + vaklue """
        
"""Write a Python program that partitions this dictionary into two sub-dictionaries:
admittedStudents whose keys are the admitted students and the key values are the averages obtained (average greater than or equal to 10).
nonAdmittedStudents whose keys are non-admitted students and the key values are the averages obtained (average less than or equal to 10)."""

students = {"student_1" : 13 , "student_2" : 17 , "student_3" : 9 , "student_4" : 15 , 
			 "student_5" : 8 , "student_6" : 14 , "student_7" : 16 , "student_8" : 12 , 
			 "student_9" : 13 , "student_10" : 15 , "student_11" : 14 , "student_112" : 9 , 
			 "student_13" : 10 , "student_14" : 12 , "student_15" : 13 , "student_16" : 7 ,
			 "student_17" : 12 , "student_18" : 15 , "student_19" : 9 , "student_20" : 17 ,}

admitted = {}
non_admitted = {} 

for student, value in students.items():
    if value >= 10:
        admitted[student] = value
    else:
        non_admitted[student] = value
#print(admitted)
#print(non_admitted)
    
#why are there random missing variables in the output? 
#why is the printing all funky when printing out a string and then the values 

#print ("Admitted students:", admitted)
#print ("Students not admitted:", admitted)



"""Write a program in Python that asks the user to enter a string, 
and return him a dictionary whose keys are the characters in the string entered 
and the values are the number of occurrences of the characters in the string. 
Example if the entered string is s = 'language', the program returns the dictionary:"""

#d = {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}

#user_dict = {}
#user_input = input("Please provide a string ")
#print(list(user_input))
#user_input = list(user_input)
#user_input = user_input.split(" ")
#print(user_input)

"""for letter in user_input:
    #print(letter, "letter", type(letter))
    if letter in user_dict:
        user_dict[letter] += 1
    else:
        user_dict[letter] = 1"""
    #user_dict[letter] = count
#print(user_dict)

"""For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. The interaction should look something like this:"""

""">>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706."""


birthdays = {
    "Dima": "May 11th, 1995",
    "Slava": "March 15th, 1964",
    "Marina": "September 27th, 1963",
}

#user_input = input("Who's birthday do you want to look up? Pick from Dima, Slava, or Marina ")
#print(birthdays[user_input])
    
    
#Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.
toys = {
    'batman': 100,
    'spiderman': 400,
    'joker':700,
}


"""total_inventory = 0


for character, inventory_count in toys.items():
    if total_inventory == 0:
        total_inventory += inventory_count
    else: 
        total_inventory """
        

#print(total_inventory)

"""total_inventory = 0

for inventory_count in toys.values():
    total_inventory += inventory_count
        

print(total_inventory)"""

"""total_sum = sum(toys.values()) 
print(total_sum)"""


#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements 
less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user."""

"""user_answer = int(input("Choose a number, any number under 100 "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_list = []
for number in a:
    if number < user_answer:
        a_list.append(number)
print(a_list)"""

#password generator 

