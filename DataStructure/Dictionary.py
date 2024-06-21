my_dictionary = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(my_dictionary)
# o/p:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(my_dictionary["brand"]) #o/p:Ford

print(len(my_dictionary)) #o/p:3

print(type(my_dictionary)) #o/p:<class 'dict'>

dictionary = dict(name="Khushbu",age=22, country="India")
print(dictionary) #o/p:{'name': 'Khushbu', 'age': 22, 'country': 'India'}

x = dictionary["name"]
print(x) #o/p:Khushbu

print(my_dictionary.get("model")) #o/p:Mustang

print(my_dictionary.keys()) #o/p:dict_keys(['brand', 'model', 'year'])

dictionary["Branch"]="Computer"

print(dictionary) #o/p:{'name': 'Khushbu', 'age': 22, 'country': 'India', 'Branch': 'Computer'}

x=my_dictionary.values()
print("Before:",x) #o/p:dict_values(['Khushbu', 22, 'India', 'Computer'])

my_dictionary["year"]=2000

print("after:",x)

print(my_dictionary)

print(my_dictionary.items()) #each item return as tupple
#o/p:dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2000)])

x = my_dictionary.items()
print("before change:" ,x) #before change: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2000)])

my_dictionary["year"]=2003

print("after change:" ,x) #after change: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2003)])

if "model" in my_dictionary:
    print("model is present in dictionary")

#change items
my_dictionary["year"]=2004

my_dictionary.update({"year":2001})
print(my_dictionary)

#Adding items
my_dictionary["color"]="Blue"
print(my_dictionary) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2001, 'color': 'Blue'}

my_dictionary.update({"price":600000})
print(my_dictionary) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2001, 'color': 'Blue', 'price': 600000}

my_dictionary.pop("price")
print(my_dictionary) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2001, 'color': 'Blue'}

my_dictionary.popitem()
print(my_dictionary) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2001}

# del my_dictionary["model"]
# print(my_dictionary) #{'brand': 'Ford', 'year': 2001}

# my_dictionary.clear()
# print(my_dictionary)


#Loop


for x in dictionary:
    print(x,dictionary[x])
print()
for x in dictionary.values():
    print(x)
print()

for x in dictionary.keys():
    print(x)
print()

for x,y in dictionary.items():
    print(x,y)

#copy of dictionary

dict_copy = my_dictionary.copy()
print(dict_copy) #o/p:{'brand': 'Ford', 'year': 2001}

my_dictionary["year"]=1994

print(dict_copy) #o/p:{'brand': 'Ford', 'model': 'Mustang', 'year': 2001}

copy_dict= dict(my_dictionary)
print(copy_dict) #o/p:{'brand': 'Ford', 'model': 'Mustang', 'year': 1994}

my_dictionary["year"]=2000

print(copy_dict) #o/p:{'brand': 'Ford', 'model': 'Mustang', 'year': 1994}

#A dictionary can contain dictionaries, this is called nested dictionaries.

student ={
    "student1":{
        "id":1,
        "name":"Khushi"
    },
    "student2":{
        "id":2,
        "name":"Tisha"
    },
    "student3":{
        "id":3,
        "name":"Rohan"
    }
}
print(student)
print(student["student2"]["name"])

for x , obj in student.items():
    print(x)

    for y in obj :
        print(y,':',obj[y])

x = my_dictionary.setdefault("year","Bronco")
print(x)
print(my_dictionary)

