#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

"""Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import re 
import string

import random
randomthing = random.seed(a=None, version=2)

PASSWORD_CHARACTERS =  string.ascii_letters + string.punctuation + string.digits
#print(randomthing)

#shuffle = random.shuffle(1[1,2])
#print(shuffle)


#validations 
#must contain 1 special characters
#must contain 1 uppercase letter 
#use mutuable data structure like a list 
#random.sample would be assigned to a list, meet the validations 

#word = list[word]

#using while loop to re enter the data 
#using dictionary to validate the input 
#calling a function inside of a function 

def password_generator():
    while True:
        password_strength = input("How strong do you want your password to be? Weak, Medium, Strong ")
        password_length = 0
        password_strengths = {
            "Weak": 6,
            "Medium": 10,
            "Strong": 15,
        }
        if password_strength not in password_strengths.keys(): #if this is false it goes to break 
            print("Invalid input, the input must be 'Weak, Medium, or Strong'")
            continue
        break
        
    return password_strengths[password_strength]

def generate_random_string(length):
    sample = random.sample(PASSWORD_CHARACTERS, length)
    sample_password = "".join(sample)
    return sample_password
    

#print(password_generator())

def is_password_valid(password_input):
    if not re.search("[a-z]", password_input):
        return False
    if not re.search("[A-Z]", password_input):
        return False
    if not re.search("[0-9]", password_input):
        return False
    if not re.search("[!@#$%^&*()]", password_input):
        return False

    return True 


#print(password_validation("123fkjF!"))
        
#steps should be as follows:
"""
    1. user enter input weak, medium, or strong 
    2. function check if input is correct string or not, throws error if not valid 
    3. if initial input is valid, input will be checked against password validation 
    4. if password validation is not valid, then we need to re run random.sample function (seems like this will need to be broken into a separate function)
    5. if password validation is valid, the password is generated and the output is printed 
    
    
    """
        
def main():
   password_length = password_generator()
   while True:
       generated_string = generate_random_string(password_length)
       if not is_password_valid(generated_string):
           continue
       break
   print(generated_string)
   
   
   #password_input = password_generator()
    
    


if __name__ == "__main__":
    main()
    
# import string
# string.ascii_letters
# string.printable





#can replace the inputs with a dictionary
"""
def password_generator():
    password_strength = input("How strong do you want your password to be? Weak, Medium, Strong ")
    password_length = 0
    password_strength = {
        "Weak": 6,
        "Medium": 10,
        "Strong": 15,
    }
    if password_strength == "Weak":
        password_length = 6
    elif password_strength == "Medium":
        password_length = 10
    elif password_strength == "Strong":
        password_length = 15
    else:
        print("Invalid input, the input must be 'Weak, Medium, or Strong'")
        
    sample = random.sample(PASSWORD_CHARACTERS, length)
    sample_password = "".join(sample)
    return sample_password
    
    return generate_random_string(password_length)"""