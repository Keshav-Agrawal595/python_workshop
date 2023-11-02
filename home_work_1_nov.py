# Ques 1 : Write a python program to get a dictionary from an object's fields...

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("Alice", 25, "New York")

dictionary = person.__dict__

print(dictionary)

# Ques 2 : Write a Python program to print a dictionary in table format.

student={
    "name  ":"Ram",
    "age   ":"Infinite",
    "grade ":"A++",
    "city  ":"Mathura"
}
for key,value in student.items():
    print(f"{key} | {value}")

# Ques 3 : Write a Python program to map two lists into a dictionary.

l1=["name","age","grade","city"]
l2=["Ram","Infinite","A++","Mathura"]
d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)

# Ques 4 : Write a Python program to get the maximum and minimum values of a dictionary.

d={"A":15,"B":70,"C":60,"D":43,"E":30,"F":2}
print(d)
print(f"The maximum value is : {max(d.values())}\nThe minimum value is : {min(d.values())}")
