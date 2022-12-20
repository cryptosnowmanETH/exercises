#return the average value of everything inside a list 

"""def average_value(*numbers): 
    return sum(numbers) / len(numbers)

print(average_value(1,2,4,5,7,8,10))"""

#use a dictionary to help remove all words that are duplicates from a string 
#idea 1: use a dictionary and name each key word1, word2, and 
colorful_sentence = "Colors bounced around in her head. They mixed and threaded themselves together. Even colors that had no business being together. They were all one, yet distinctly separate at the same time. How was she going to explain this to the others?"


"""def countwords(*word_count):
    for word in word_count:
        return word.count()
print(countwords(['Colors bounced around in her head. They mixed']))"""
    

"""def remove_duplicates(sentence):
    cleandict = {}
    for word in sentence.split(" "):
        if word in cleandict:
            cleandict[word] = cleandict[word] + 1
        else: 
            cleandict[word] = 1
    cleandict_copy = cleandict.copy()
    for word, word_count in cleandict_copy.items():
        if word_count > 1:
            del cleandict[word] 
    return cleandict

print(remove_duplicates(colorful_sentence))
"""

#never write a function that depends anything outisde of the funciton 
def multiply(numbers):
    value_multiplied = 1 
    for value in numbers:
       value_multiplied = value * value_multiplied
    return value_multiplied

print(multiply([1,2,3,8]))