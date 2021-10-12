
#spacing **
if( 5> 2):
    print("five is greater than two")

if( 5> 2):
        print("five is greater than two")

#commenting is through the use of '#'

#if else
x = 5
y =2
z = 3
if  x > y:
    print("x > y")
elif x> y & x>z:
    print("x is the biggest")
else:
    print("not the conditions we specified")

#variable **
x = 5
y = "Hello"

#data type **
#typical data types
x = "hello" #string
y = 3 #whole number
z = 2.8

total = y + z #will not work
print(total)
#check the data type here
print(type(total))


###################################
#list 
fruits = ["apple", "banana", "pear"]
print(len(fruits))

mixedlist = ["apple", 3, "orange", 4.2, "pear"]
#accessing it
print(mixedlist[0])
print(mixedlist[-1])
print(mixedlist[1:3])
print(mixedlist[-3:-1])

#check if it exists
if "apple" in mixedlist:
    print("iphone13") #return true

#insert only
fruits = ["apple", "banana", "pear"]
#position, item 
fruits.insert(1,"watermelon") #["apple", "watermelon", "banana", "pear"]
#remove item
fruits = ["apple", "watermelon", "banana", "pear"]
fruits.remove("watermelon")  #fruits = ["apple", "banana", "pear"]
fruits.pop(1) #fruits = ["apple", "banana", "pear"]



#replace 2 item with 1 item
fruits = ["apple", "watermelon", "banana", "pear"]
fruits[1:3] = ["banana"]
print(fruits)  # ["apple", "banana", "pear"]



###################

#for loop
fruits = ["apple", "banana", "pear"]
for x in fruits:
    print(x)

for x in range(3):
    print(x)


#############
#function **
x = 2
y = 3
total = 0 
def myfunction( a,b):

    total = a+b
    print("result =" + total )
    # return total

myfunction(x,y)
#Scope
print(total) 


