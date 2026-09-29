def beeramid(bonus, price):
    result, i = 0,0
    if bonus<=0 or price<=0:
        return 0
    while result <= (bonus//price):
        i+=1
        result+=(i**2)
        
    return i-1


print(beeramid(-4,1))