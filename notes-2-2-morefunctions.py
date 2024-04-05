# more functions 
# author: odyssa 
# 4 april 2024

def stars(num_stars: int) -> str:
    """returns a given number of *"""
    value = ""
   
   #if the value == 0 or value == 1 "*"
    # if value > 1 "*" * num_stars
    #else negative number -> error
    if num_stars == 0 or num_stars == 1:
        value = "*"
    elif num_stars > 1:
        value = "*" * num_stars 
    else:
        value = "sorry, can't take negative numbers"
  
    return value


# multiply stings 
# greeting = "hello"
# print(greeting * 2)

# print("the quick brown fox jumps over the lazy dog." * 2)
print(stars(1)) # "*"
print(stars(100)) 
print(stars(0))
print(stars(-1))