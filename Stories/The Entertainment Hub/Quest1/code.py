import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("/home/krisje/Projects/everybody.codes/")
from AOCHelper import * 
grid = tokens = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}/{filename}"
    global grid, tokens
    grid,tokens = readinput_arrays_by_newline(filename)

def main():
   readinput("notes3_ex.txt")
   #first_star()       
   #second_star()
   third_star()
        
def first_star():
    coins =  0
    maxx = len(grid[0])
    slots = [i for i in range(len(grid[0])) if i % 2 == 0]
    for idx, slot in enumerate(slots):
        coins += drop_token(tokens[idx], slot, idx, maxx)
        
    print(f"Result First Quest: {coins}")

def drop_token(behaviors, slot,idx,maxx):
    row_idx = 0
    coins = 0
    coin = slot
    done = False
    while row_idx <= len(grid):
        if done:
            return coins
        for token in behaviors:
            if done:
                return coins
            token = 1 if token == "R" else -1 
            if row_idx == 0:
                token = 1 if slot == 0 else -1 if slot >= maxx - 1 else token
            if coin <= 0 and token == -1:
                token = 1
            if coin >= maxx - 1 and token == 1:
                token = -1
            coin += token
            while grid[row_idx][coin] != "*":
                row_idx += 1
                if row_idx >= len(grid):
                    coins += count_coins(coin, idx)
                    done = True
                    return coins
    return coins
def count_coins(coin, slot):
    coins =  (coin//2+1) * 2 - slot
    return 0 if coins < 1 else coins -1 

def second_star():
    coins =  0
    maxx = len(grid[0])
    slots = [i for i in range(len(grid[0])) if i % 2 == 0]
    
    for behaviors in tokens:
        results = []
        for idx, slot in enumerate(slots):
            row_idx = 0
            coin = slot
            done = False
            while row_idx <= len(grid):
                if done:
                    break
                for token in behaviors:
                    if done:
                        break
                    token = 1 if token == "R" else -1 
                    if row_idx == 0:
                        token = 1 if slot == 0 else -1 if slot >= maxx - 1 else token
                    if coin <= 0 and token == -1:
                        token = 1
                    if coin >= maxx - 1 and token == 1:
                        token = -1
                    coin += token
                    while grid[row_idx][coin] != "*":
                        row_idx += 1
                        if row_idx >= len(grid):
                            results.append(count_coins(coin, idx))
                            done = True
                            break
        coins += max(results)
        #print(f"Max coins for behavior {behaviors}: {max(results)}") 
     

    print(f"Result Second Quest: {coins}")

def third_star():
   
    results = []
    maxx = len(grid[0])
    c = len(grid[0])
    print(f"Each token has {c} possible slots to drop in")
    slots = [i for i in range(len(grid[0])) if i % 2 == 0]
    print(f"Possible slots: {slots}")
    slots = list(itertools.permutations(slots, 6))
    print(f"Total combinations to check: {len(slots)}")
    for tuple in slots:
        coins = []

        for idx, slot in enumerate(tuple):
            coins.append(drop_token(tokens[idx], slot, idx, maxx))
        results.append(max(coins))
    print(f"Max coins: {max(results)}")
    print(f"Min coins: {min(results)}")

def third_star_old():
    maxi,mini =  0,0
    maxx = len(grid[0])
    slots = [i for i in range(len(grid[0])) if i % 2 == 0]
    combinaties = list(itertools.permutations(range(17), 6))
    

    for behaviors in tokens[:6]:
        print(behaviors)
        results = []
        for combinatie in combinaties:
            for idx, slot in enumerate(combinatie):
                row_idx = 0
                coin = slot
                done = False
                while row_idx <= len(grid):
                    if done:
                        break
                    for token in behaviors:
                        if done:
                            break
                        token = 1 if token == "R" else -1 
                        if row_idx == 0:
                            token = 1 if slot == 0 else -1 if slot >= maxx - 1 else token
                        if coin <= 0 and token == -1:
                            token = 1
                        if coin >= maxx - 1 and token == 1:
                            token = -1
                        coin += token
                        while grid[row_idx][coin] != "*":
                            row_idx += 1
                            if row_idx >= len(grid):
                                results.append(count_coins(coin, idx))
                                done = True
                                maxi += max(maxi, max(results))
                                mini += min(mini, min(results))
                                break
            
    print(f"min: {mini} max: {maxi}")
     

if __name__ == '__main__':
    main()