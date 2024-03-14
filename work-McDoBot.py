# McDoBot
# Author: Odyssa Yip
# 22 Feb 2024 

fries = input("would you like fries with your meal?  (Yes/No)")

if fries.lower().strip("!.?, ") == "yes":
    print("here's your meal with you fries!")

elif fries.lower().strip("!.?, ") == "no":
    print("here's your meal without fries!")

else:
    print(f"sorry, i don't understand {fries}.")