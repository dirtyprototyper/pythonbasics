#page 3: Data types
x = "a random string"
print(type(x))

#int
y = 5
print(type(y))

#float
pie = 3.15
print(type(pie))

#list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#dictionary
x = {"name" : "John", "age" : 36}
print(type(x))

#boolean
covid = False
print(type(covid))

#page4: If-else Statement
today = "Home-Based Learning"
tomorrow = "Public Holiday" 

'''
uncomment accordingly to test
today = "Saturday"
yesterday = "Friday"
'''
if today == "Saturday":
    print("No School")

elif today == "Sunday" or tomorrow == "Public Holiday":
    print("No School")

else:
    print("Going To School")

#page 5: declaring array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# Adding item to the array 
cars.append("Honda")

# Removing elements to the array
cars.pop(4)
cars.remove("Honda")

#page 6: For loop
for x in range(3):
    #print from 0 to 2	
    print (x) 

for x in range(2,6):
    #print from 2 to 5	
    print(x)

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

#page 7: Dictionary
thisAppleProduct =	{
    "brand": "Apple",
    "type": "Macbook",
    "year": 2013,
    "year": 2015,
    "color": ["grey", "pink","light grey"]
}

print(thisAppleProduct["year"]) #returns 2015

print(thisAppleProduct.keys())  #returns all the keys
print(thisAppleProduct.values())  #returns all the value
                            
#changing specific values
thisAppleProduct["type"] = "IPhone"
print(thisAppleProduct["type"]) #return IPhone

#page 8: Function
x = "parameter"
y = "arguments"

def my_function (arg1, arg2):
    #refer to the arguments according to what you called it as in the parameters
    print(arg1 + " is the same as " + y)


#to invoke the function
my_function(x,y)

#example 2
number1 = 2
number2 = 3
total = 0

def sum(num1, num2):
    total = num1 + num2

sum(number1, number2)	
print(total) # Is this 0 or 5?

def sum(num1, num2):
    total = num1 + num2	
    return total	

sum(number1, number2)	
print(total) #is this 0 or 5

#example 3
mylist = ["chocolate", "apple", "soda"]

def shopping(grocerylist):
    for x in grocerylist:
        print(x)	

shopping(mylist)

#page 9 Class & Object

#Example 1: Defining a class
class Human:
    eye = 2,
    hair = "black"

#creating the object
Adam = Human()

#hair is known as property
print(Adam.hair) #return black

#changing the property value 
Adam.hair = "blonde"
print(Adam.hair) #return blonde

#Example 2: 
class Human:
    #assign value for name and age accordingly
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Human("John",21)
print(person.name)

#Example 3:
class Human:
    #assign value for name and age accordingly
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Greetings():
        print("hello there")

person = Human()
person.Greetings()

