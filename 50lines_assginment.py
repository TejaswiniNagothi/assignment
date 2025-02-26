# Variables and Strings
name = "Riya"
age = 25
city = "New York"
message = f"{name} is {age} years old and lives in {city}."
print(message)

# Lists 
fruits = ["apple", "banana", "cherry","pappaya"]
print(fruits)

# append method
fruits.append("orange")
print(fruits)

# insert method
fruits.insert(1, "grape")
print(fruits)

# remove method
fruits.remove("banana") 
print(fruits)

#count method
veg=["carrot","potato","cabbage","carrot","potato","carrot","brinjal","carrot","potato"]
x=veg.count("carrot")
print(x)

#clear method
data=["jan","feb","mar","apr","may"]
data.clear()
print(data)

# Tuples
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","saturday")
print("my favourate day in week is:", days[5])

# Dictionaries
person = {"name": "Riya", "age": 25, "city": "New York"}
print("Age:", person["age"])
person["age"] = 26  
person["profession"] = "Engineer"  
print(person)

# Conditional Statements
# if-else
if person["age"] > 18:
    print("Riya is an adult.")
else:
    print("Riya is a minor.")

# elif
menu={
    "ice-creams":["vanilla icecream","chocolate icecream","butter pecan icecream","strawberry icecream"],
    "chocolates":["5star","dairy-milk","milk chocolate","dark chocolate"]
    }
order=input("enter your order:")
if order in menu["ice-creams"]:
    print(f"your order {order} is available in ice-cream menu")
elif order in menu["chocolates"]:
     print(f"your order {order} is available in chp=ocolates menu")
else:
     print(f"sorry {order} is not available")
             

# Concatenate
a= [1, 2, 3]
b= [4, 5, 6]
concatenated= a+b
print("Concatenated List:", concatenated)

# List Methods 
numbers = [10, 20, 30, 40, 50]
numbers.pop()   
numbers.reverse()   
print(numbers)

#accessing the list a array
fruits=["apple","banana","papaya","kiwi","orange"]
print(fruits[1:4])
vegetables=["carrot","potato","cabbage","brinjal"]
print(vegetables[:3])


