#https://www.w3schools.com/python/python_dictionaries_exercises.asp

#Use the get method to print the value of the "model" key of the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get('model'))


#https://pynative.com/python-dictionary-exercise-with-solutions/
#Exercise 1: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]

new_dict = {}
for values in keys:
    for value in values: 
        new_dict[values] = value
print(new_dict)


#expected output 

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}