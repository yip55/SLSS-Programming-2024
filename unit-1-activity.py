# who's the best driver 
# author: Odyssa Yip
# date: march 4

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
        

driver = input("who's the best F1 driver ever?")

result = best_driver(driver)
print(result)


