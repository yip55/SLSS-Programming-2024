#methods string
# Author: odyssa 
# 22 feb 2024 

# Ask the user what is the waether like
weather = input("what's the weather like?")

# if they repy rainy 
    # Bring an umbrella 

if weather.lower().strip("!.?, ") == "rainy":
    print("you'll need an umbrella")
else:
    print(f"sorry, i don't understand {weather}.")