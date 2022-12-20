# Change Plato's birth year from B.C. 427 to B.C. 428.

dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

#Type your answer below.
dict['born'] = 428 

#print(dict["born"])


"""Dictionaries can have nested data too. Also, you can add a new key to a dictionary as they are mutable (changeable). Try to add the key "work" to dict with values shown below.


"work": ["Apology", "Phaedo", "Republic", "Symposium"]"""

dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
dict['work'] = ["Apology", "Phaedo", "Republic", "Symposium"]
#print(dict)


""".get() method can be used just to get the value of a key. But it has more tricks up its sleeve.


Try to look for key: "son's age" and if nothing comes up make the .get() return "2".

"""


dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Type your answer here.
ans_1= dict.get('2')
if not (ans_1 > 1):
    print(ans_1)
