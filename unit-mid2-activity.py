# unit 1/2 activity 
# Author: odyssa yip
# april 9 2024

def best_driver(driver):
        
    if driver.lower().strip("!.?, ") == "lewis hamilton":
        return"CORRECT!"
    if driver.lower().strip("!.?, ") == "max verstappen":
        return"WRONG! Absolutely not"
    if driver.lower().strip("!.?, ") == "kimi raikonnen":
        return"okay, maybe"
    if driver.lower().strip("!.?, ") == "sebastian vettel":
        return"Yes"
    if driver.lower().strip("!.?, ") == "ayrton senna":
        return"of course"
    else:
        return"ummm, I don't think so"
        




user_answer = input("who's the best F1 driver ever?").lower().strip("!.?, ")

while user_answer not in ["lewis hamilton", "max verstappen", "ayrton senna", "kimi raikonnen", "sebastian vettel"]:
    user_answer = input("i don't think so? seriously, who's the best F1 driver ever? ").lower().strip("!.?, ")

print(best_driver(user_answer))