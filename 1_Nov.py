# name=input("Enter your name :")
# print(f"The length of the {name} is : {len(name)}")


# age = 5
# if age>=18:
#     print("You're an Adult")
# else:
#     print("You're still Minor")


# score=85
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# else:
#     print("F")

# is_raining=True
# is_cold=True

# if is_raining:
#     print("Bring an Umbrella")
#     if is_cold:
#         print("Wear a Jacket")


# number=10
# if number>0:
#     print("The number is positive")
# else:
#     print("The Number is negative")


# number=0
# if(number>0):
#     print("the number is positive")
# elif number<0:
#     print("the number is negative")
# else:
#     print("The number is zero")


'''
set is an unordered collection of unique elements in python
defined by emnclosing elements in {} braces using the set() constructor 
'''

# my_set={1,2,3}
# my_set.add(4)
# print(my_set)

# my_set.remove(2)
# my_set.discard(5)
# print(my_set)

# my_set1={89,90}
# my_set=my_set.union(my_set1)
# print(my_set)


# set1={2,4,6,8,10}
# set2={1,2,3,5,7,9}
# print(set1.intersection(set2))

# print(set1.difference(set2))

'''

OOPS
_init_ method is a special method used to initialise the object when it's created.

self is a reference of the current instance of the class.

self is used  the _init_ method to refer to the instance being created--> in the objects and classes example 

'''

# class Dog:
#     def __init__(self,name):
#         self.name=name

# dog1=Dog("Buddy")
# print(dog1.name)

'''
classes in python are like blueprint for creating objects..
'''

# class Car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model

# car1=Car("Toyota","Camry")
# car2=Car("Honda","Civic")

# print(car1.make, car1.model)  # Output: Toyota Camry
# print(car2.make, car2.model)  # Output: Honda Civic


#  Encapsulation -->
'''
    is a concept that restricts access to certain part of an object.
    mark members as private by using the double underscore(__).

'''
# Encapsulation Example 

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_number = account_number   # Protected member 
#         self._balance = balance   # Private member
    
#     def get_balance(self):
#         return self._balance

# account1=BankAccount("12345",1000)
# print(account1._account_number)  # Accessing a protected member
# print(account1.get_balance())    # Accessing a private member using a method

# Inheritance concept

'''
    Inheritance allows you to create new classes that inherits properties and methods from existing classes..
'''

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog=Dog("Buddy")
# cat=Cat("Whiskers")

# print(dog.name, dog.speak())   # Output : Buddy Woof!
# print(cat.name, cat.speak())    # Output : Whiskers Meow!


# employees=['Corey','Jim','Steven','April','Judy','Jenn','John','Jane']
# gym_members=['April','John','Corey']
# developers=['Judy','Corey','Steven','Jane','April']

# gym_set=set(gym_members)
# develop_set=set(developers)

# intersect=gym_set.intersection(develop_set)
# print(intersect)

# Symmetric difference and difference 

# s1={1,2,3}
# s2={3,4,5}
# s3={4,5,6}

# s4=s2.difference(s1)
# s5=s2.symmetric_difference(s1)  # Symmetric difference is the intersection of the 2 sets and then the union of the remaining all elements..

# print(s4)
# print(s5)

# Dictionary

# student={
#     "name":"Alice",
#     "age":25,
#     "grade":"A"
# }

# print(student.get("name"))  # output is Alice
# print(student.get("phone"))  # output is None

# student["age"]=26
# student["city"]="New York"

# print(student)
# print(student.items())

# for key,value in student.items():
#     print(f"{key} : {value}")

# for key,value in student.items():
#     print("{key} : {value}")
# print(student.keys())
# print(student.values())

# grade = student.get("grade","N/A")
# print(grade)

# del student["age"]
# print(student)

# student["address"]="mathura"

# print(student.get("address"))


# squares={num:num**2 for num in range(1,6)}
# print(squares)


# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# d={'x':10,'y':20,'z':30}
# for x,y in d.items():
#     print(f"{x} : {y} ")

# n=int(input("Enter Number :"))
# dict={num: num**2 for num in range(1,n+1)}
# print(dict)

# dict={num: num**2 for num in range(1,16)}
# print(dict)

# my_dict={'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))

# color_dict={
#     'red':'#FF0000',
#     'green':'#008000',
#     'black':'#000000',
#     'white':'#FFFFFF'
# }
# l=color_dict.keys()
# l1=sorted(l)

# for i in l1:
#     print(f"{i} : {color_dict[i]}")

# # Alternate Method :

# for key in sorted(color_dict):
#     print(f"{key} : {color_dict[key]}")

d={1:10,2:20,3:30,4:40,5:50,6:60}
n=eval(input("Enter element to search :"))
if n in d:
    print("Found successfully")
else:
    print("not found")
