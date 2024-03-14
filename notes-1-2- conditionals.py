# conditionals
# author : odyssa 
# 15 feb 2024

# favourite_book = input("what's your fav book?")
# print("oh, that's a nice book!")

# three_wishes = ("height", "stregth", "beauty")
# print(three_wishes)

#impliment flowchart from notes
x = 1_000_000
y = -5.7

# if x is less than y. say so
# if x is greater than y, say so
# if x is equal to y, say so

# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

foo = int(input("enter a number:"))  # sting

if int(foo) < -1 or int(foo) == 0: 
    print("foo is less than 1")
    print("or it's equal to zero")

# check if foo is inside a range 
# Greater than one and less than 1000
if foo > 1 and foo < 1000:
    print("foo is in the range 2 - 999")
else:
    print("foo is outside the range 2 - 999")