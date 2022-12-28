#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

"""Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import random
randomthing = random.seed(a=None, version=2)
#print(randomthing)

#shuffle = random.shuffle(1[1,2])
#print(shuffle)


#validations 
#must contain 1 special characters
#must contain 1 uppercase letter 
#use mutuable data structure like a list 
#random.sample would be assigned to a list, meet the validations 

#word = list[word]

def password_generator():
    password_strength = input("How strong do you want your password to be? Weak, Medium, Strong ")
    password_length = 0
    if password_strength == "Weak":
        password_length = 6
    elif password_strength == "Medium":
        password_length = 10
    elif password_strength == "Strong":
        password_length = 15
    else:
        print("Invalid input, the input must be 'Weak, Medium, or Strong'")
    sample = random.sample("abcdetfghijk1mnopqrstuvwxyz1234567890!@#$%^&*()", password_length)
    sample_password = "".join(sample)
    return sample_password

print(password_generator())

def password_validation(password_input):
    if not password_input == "Weak":
        print()
        
# import string
# string.ascii_letters
# string.printable