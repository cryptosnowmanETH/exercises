"""Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]."""

letters = "woeirjf"
"""for letter in letters:
    
    print(letter)"""

def capitalLetters(stringinput):
    letterlist = []
    letterindex = [] 
    for letter in stringinput:
        if letter.isupper():
            letterindex.append(stringinput.find(letter))
    return letterindex

#print(capitalLetters("HeLlO"))


"""Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online."""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Evan": "online",
}

"""online = 0 

for people, status in statuses.items():
    if status == "online":
        online += 1
        continue
print(online)"""

def online_count(isOnline):
    online = 0 
    for status, people in isOnline.items():
        if people == "online":
            online += 1
    return online 

#print(online_count(statuses))

"""3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

"""Example 1: Displaying the Keys in sorted order
In this example, we are trying to sort the dictionary by keys and values in Python. Here, iterkeys() returns an iterator over the dictionary’s keys.


Input:
key_value[2] = '56'       
key_value[1] = '2'
key_value[4] = '12'
key_value[5] = '24'
key_value[6] = '18'
key_value[3] = '323'

Output:
1 2 3 4 5 6 """



"""Example 5: Sort Dictionary By Value in Python
In this example, we are trying to sort the dictionary by values in Python. Here we are using dictionary comprehension to sort our values."""

"""Input:
key_value['ravi'] = 10       
key_value['rajnish'] = 9
key_value['sanjeev'] = 15
key_value['yash'] = 2
key_value'suraj'] = 32

Output:
{'ravi': 2, 'rajnish': 9, 'sanjeev': 10, 'yash': 15, 'suraj': 32"""


"""Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'"""

"""front = "code"
front_replaced = front[-1] + front[1:-1] + front[0]
print(front[:-1])
print(front[-1])
print(front[1:-1])
print(front[1])
print(front_replaced)"""


front_back = 'code'

def changeLetters(anystring):
    correctedstring = anystring[-1] + anystring[1:-1] + anystring[0]
    return correctedstring

#print(changeLetters("dave"))

def front3(anystring):
    correctedstring = anystring[0:3]*3
    return correctedstring
#print(front3('Java'))
#print(front3('Chocolate'))
#print(front3('abc'))


"""Write a Python script to add a key to a dictionary."""

def appendKey(anydict):
    newPair = {0: 10, 1: 20}
    #newPair = newPair.update(anydict)  = {2:30}// this doesn't work will return none 
    newPair.update(anydict)
    newPair[0]=5
    return newPair
#print(appendKey({2:30, 4:30, 5:30}))

#Adding new key value pair in a dictionary through a loop 
def appendKey(anydict):
    newPair = {0: 10, 1: 20}
    #newPair = newPair.update(anydict)  = {2:30}// this doesn't work will return none 
    for key, value in anydict.items():
        newPair[key] = value 
    return newPair
#print(appendKey({2:30}))

"""Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""


#removing a key value pari 
names_ages = {
    'jeremy' : 42,
    'andrew': 39,
    'brad': 19,
}

names_ages.pop('jeremy')
print(names_ages)

