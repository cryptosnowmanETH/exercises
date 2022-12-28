#two components: functions (behavior) and data (gives knowledge) 
#functions should be name with verbs 
#class is a concept and is always named with a noun like bank_account or employee
#contain behaviors and definitions of the data that are grouped together to make your program easier to manage 

#you can do anything inside a class as long as its in a function 

class Vehicle:
    #this is a member function. any variable that is an instance of a vehicle class can now acceess the vehicle classes member functions
    
    #self is the name space of the instance 
    # "dunders" __init__, these are executed without being called by the programmer 
    #init is a initializer, it initializes variables with values 
    # a constructer builds and initializes instances of classes 
    wheels = 4 #only declare class level variables in cases where every function will have the same variable value 
    
    def __init__(self,make,color):
        self.make = make 
        self.color = color
    
    @classmethod #does not belong to the instance, belongs to the class and it allows to be called without the instance 
    def build_four_wheel_drive(cls):
        return cls(tools, build)    
        
    def sound_horn(self):
        print("beep")
        
    def brake(self):
        print("brake the car", self.make)

my_new_car = Vehicle.build_four_wheel_drive(tools, build)

#to use the class 
#ford is actually a dict type. ford variable is a type of vehicle. Ford is an instance of the vehicle class.
#this is called "instantiating a vehicle"
car1 = Vehicle('ford','red')
#print(car1.make)
#print(car1.color)

#calling the ford instances sound_horn function 
#car1.sound_horn()

#each instance can store different data 
car2 = Vehicle('bmw','black')
car2.brake()


