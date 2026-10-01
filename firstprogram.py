# for single line comment control + slash
""" 
for multi line code shift + alt + a  
"""
# python is dynamically typed language
name = "alex"
age = 20
location = "kathmandu"
# concate
print("my name is " + name + " age is " +str(age) + " and location is " + location)
# string
print(f"my name is {name}  age is {age} and location is {location}")
# format old version
print("my name is %s  age is %d and location is %s" %(name, age, location))
# format new version 
print("my name is {0}  age is {1} and location is {2}" .format(name, age, location))

print((type(location)))

Name = input("Enter the name ")
Age = int(input("Enter the age"))
Location = input("Enter the location")
# concate
print("my name is " + Name + " age is " +str(Age) + " and location is " + Location)
# string
print(f"my name is {Name}  age is {Age} and location is {Location}")
# format old version
print("my name is %s  age is %d and location is %s" %(Name, Age, Location))
# format new version 
print("my name is {0}  age is {1} and location is {2}" .format(Name, Age, Location))

num1 = input("Enter your first name ")
num2 = input("Enter your last name ")
sum1 = num1 + num2
print(f"the sum is {sum1} and type is {type(sum1)}")
num3 = int(input("Enter the number"))
num4 = int(input("Enter the number"))
sum2 = num3 + num4
print(f"the sum is {sum2} and type is {type(sum2)}")
