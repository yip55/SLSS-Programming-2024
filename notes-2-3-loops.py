# loops and iteration
#author: odyssa 
# 5 april 2024

# print "something" 10 times
for _ in range(10):
    print("something")

# create a grocery list
# do something for each item in the list 
grocery_list = [
    "blueberry muffins",
    "potato chips",
    "alumimium foil",
    "orange juice",
    "RTX 4070 super",
    "cereal"
]

# for every item on the list:
#       *{grocery item}
#       *{grocery item}
#       *{grocery item}
for item in grocery_list:
    # skip the rest of the list
    # if we get to RTX 4070 super
    if item.lower() == "rtx 4070 super":
        print("Mr. ubial can't buy a 4070!")
        break #stop looping 
    print(f"* {item}")

# can you count using a for loop?
# use a for lop to count to 100
for i in range (10):
    print(i + 1)

# this loops repeats indefinetley

# while true: 
#     print("This is an infinite loop")

# while loops are useful for input valudation 
# ask the user if they like ice cream
#    if they don't answer yes or no 
#         repeat the question 

user_answer = input("Do you like ice cream?").lower().strip("!.?, ")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input("seriously, do you like ice cream?").lower().strip("!.?, ")

if user_answer in["yes", "yeah"]:
    print("Nice. I love ice cream, too.")
elif user_answer in ["no", "nah"]:
    print("how could you not like ice cream?")