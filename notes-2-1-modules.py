# modules
# author: odyssa 
# 11 march 2024

import random

# demostrate some parts of the random module
# random.random() -> (0, 1.0]

def coin_flip():
    # return either heads, tails, or other?
    # heads -- (0 - 0.5]
    #tails -- (0.5, 0.999999]
    # other --- the rest
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "other"
# def draw_card():
#     # simulate drawing a card
#     # return a card value from A, 2 , 3, ...., Q, K 
#     # random.randrange() -> int in some range
#     result = random.randrange(1, 14)

#     if result == 1:
#         return "A"
#     elif result == 11:
#         return "J"
#     elif result == 12:
#         return "Q"
#     elif result == 13:
#         return "K"
     
    
def main():
    # repeat the coin flip 1000 times
    #keep track of heads, tails, and other
    heads = 0
    tails = 0
    others = 0

    # drawn_card = []


    for _ in range(1_000_000):
        #flip coin
        result = coin_flip()
        # drawn_card.append(draw_card())

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1   # increment
        else:
            others += 1

    # print results
    print(f"heads: {heads}")
    print(f"tails: {tails}")
    print(f"others: {others}")
    # print (drawn_card [0:100])


main()
