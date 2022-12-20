"""people = {
    'dima': 28,
    'andrew': 27,
    'tim': 19,
    'costner': 72,
}"""

sentence = "This is a long sentence called the fox jumps over a horse in the canal while snowboarding. This doesn't make sense, but this is a snowboarding exercise."


#1. Write a program that uses a dictionary to count the number of times a word appears in a long string.

"""def count_words(sentence):
    sentence_dict = {}
    count = 0 
    words = sentence.split(" ")
    for word in words:
        if word in sentence_dict:
            sentence_dict[word] += 1 
        else:
            sentence_dict[word] = 1
    return sentence_dict

print(count_words(sentence))"""


"""def count_words():
    words = sentence.split(" ")
    sentence_dict = {}
    count = 0 
    for word in words:
        if word in sentence_dict:
            sentence_dict[word] +=1
        else: 
            sentence_dict[word] = 1
    return sentence_dict

print(count_words())
"""


people = {
    'dan': 32,
    'dima': 44,
    'johnny': 67,
    'gugu': 92,
}


#Write a program that takes a dictionary that contains peoples names as keys, and their age as values. 
#Calculate the person with the lowest age, highest age, calculate the average age, and then print each persons name and age on separate lines. 
#Print the minimum, maximum and average ages below the list.

"""def lowest_age(people):
    min_age = min(people.values())
    return min_age
print(lowest_age(people))"""

"""def highest_age(people):
    max_age = max(people.values())
    return max_age 
print(highest_age(people))"""

"""def average_age(people):
    total_sum = sum(people.values()) / len(people.values())
    return total_sum 

print(average_age(people))"""








"""def highest_age(people):
     values = people.values()
     max_values = max(values)
     return max_values

print(highest_age(people))"""
    
"""def lowest_age(people):
    lowest = float("inf")
    for person, age in people.items():
        if age < lowest:
            lowest = age
    return lowest

#print(lowest_age(people))



def average_age(people):
    persons_age = 0
    number_of_people = 0
    for person, age in people.items():
        persons_age += age
        number_of_people += 1 
    average = persons_age / number_of_people
    return average
"""
#print(average_age(people))

#why is the number_of_people still 1? 

"""persons_age = 0
number_of_people = 0"""

"""def average_age(people):
    persons_age = 0 
    number_of_people = 0
    for _, age in people.items():
        persons_age += age
        number_of_people += 1
    average = persons_age / number_of_people
    return average

print(average_age(people))"""

"""def new_average_age(people):
    return sum(people.values())/len(people.values())

print(new_average_age(people))"""
#people.values and people.keys are lists 
#print(new_average_age(people))

#Several ways to loop through dictionary 
#for _, age in people.items():

"""1. Write a program that uses a dictionary to count the number of times each word appears in a long string.
2. Convert two lists, one with 10 letters, one with 10 numbers to a dictionary. The letters are keys, the numbers values.
3. Create a dictionary that stores the squares of all numbers from 1 to 199."""



#Here are 3 for tonight: # Dict exercises
#1. Write a program that uses a dictionary to count the number of times a word appears in a long string.
#2. Convert two lists, one with 10 letters, one with 10 numbers to a dictionary. The letters are keys, the numbers values.


#3. Create a dictionary that stores the squares of all numbers from 1 to 199.


"""while square < 200:
     squares = square * square """


"""for square in squares:
    
    range(1,200)"""
    
    
"""def count_words():
    words = sentence.split(" ")
    sentence_dict = {}
    count = 0 
    for word in words:
        if word in sentence_dict:
            sentence_dict[word] +=1
        else: 
            sentence_dict[word] = 1
    return sentence_dict

print(count_words())
"""

"""
def squared(): 
    count = 0
    squares = {}
    for i in range(1,200):
        count += 1
        squared = i * i
        squares[count] = squared
    return squares
print(squared())"""



#2. Convert two lists, one with 10 letters, one with 10 numbers to a dictionary. The letters are keys, the numbers values.

letter_numbers = {} 
letters = ['a','b','c','d','f','t','g','h','g','f']
numbers = [12,25,35,46,55,61,71,84,59,610]

"""def convert_to_dict():
    for letter in letters: 
        letter_numbers[letter] = None
    for number in numbers: #this can't be a nested loop 
        letter_numbers[letter] = number
    return letter_numbers 

print(convert_to_dict())
"""


def convert_to_dict():
    for letter in letters: 
        for number in numbers: #this can't be a nested loop 
            letter_numbers[letter] = number
            numbers.remove(number)
            break 
    return letter_numbers

#print(convert_to_dict())

#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}



#2. Convert two lists, one with 10 letters, one with 10 numbers to a dictionary. The letters are keys, the numbers values.

"""letter_numbers = {} 
letters = ['a','b','c','d','f','t','g','h','g','f']
numbers = [12,25,35,46,55,61,71,84,59,610]

def list_to_dict(letters,numbers): 
    letter_numbers = {} 
    for letter in letters: 
        letter_numbers['letter']
    for number in numbers: 
        letter_numbers['letter'] = number 
    return letter_numbers

print(list_to_dict(letters, numbers))"""



#3. Create a dictionary that stores the squares of all numbers from 1 to 199.

"""def store_squares():
    squares = {}
    for number in range(0,200):
        squares[number] = number * number 
    return squares

print(store_squares())"""



#1. Write a program that uses a dictionary to count the number of times a word appears in a long string.