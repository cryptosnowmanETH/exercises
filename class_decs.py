person = {'cars': 'BMW'}

assert person['cars'] == 'BMW'

person['cars'] = 'Mercedes'
person['wheels'] = 'Hot wheels'

#print(person)
#print(person.items())

for key, value in person.items():
    print(key, value)
    
"""
codes = {'a': 2, 'b': 3}

codes['a'] += 1
assert codes['a'] == 3

codes['a'] = codes['a'] + 1

try:
    codes['x'] += 4
except KeyError:
    codes['x'] = 4

print(codes['x'])

if codes.get('y', None) is None:
    codes['y'] = 1
else:
    codes['y'] += 1

assert codes['y'] == 1

denominator = 2
try:
    result = 10 / denominator
except ZeroDivisionError:
    print("cant div by zero")
    result = 10 / 1
print(result)

headings = ['col_a', 'col_b', 'col_c']
rows = [[2, 5, 7], [4, 6, 1]]

# {'col_a': 2, 'col_b': 5

print(dict(zip(headings, rows[0])))

numbers = {3, 4, 5, 6, 7, 8}

more_numbers = [
    0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8,
    2, 4, 3, 2, 43, 1
]

more_numbers = list(set(more_numbers))
print(more_numbers)
"""