# Notes - dictionaries

# Big Ideas:
#   - A dictionary is a data structure
#   - Dictionaries map keys to value

# flashback to lists
person = ["john", "23 years old", "4500 1023 2222 1111"]

# rewrite person as a dictionary
person_dict = {
    "name": "john",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111",
    "SIN num": 700_000_00
}

person_one = {
    "name": "jim",
    "age": "42",
    "cc num": "5100 2030 3884 1992",
}
# get and print the person's name(?)
# print(person[0]) # use the index

# print(person[2]) # last item in the list
# print(person[-1])

# print(person[10]) # code will break 

# grab values from a dictionary
print(person_dict["name"])
print(person_dict["cc num"])

print(person_one["name"])
print(person_one["cc num"])

#iterate over the person list
# for info in person:
#     print(info)

#iterate over the person dictionary 
#print the info
for key in person_dict:
    key
# pythonic way of iterating over a dictionary 
for key, value in person_dict.items():
    print(key,value, sep=": ")
