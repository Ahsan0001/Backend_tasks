def greedy_exchange(amount, denominations):
    coins=[0]*len(denominations)
    x=0
    
    while amount:
        if denominations[x]<=amount:
            amount = amount - denominations[x]
            coins[x]+=1

        else:
            x+=1
        
       
    return coins

#checking output
print("TASK 1 OUTPUT:\n")
print(greedy_exchange(56, [20, 10, 5, 1]))
print(greedy_exchange(350, [100, 50, 10, 5, 2, 1]))
print(greedy_exchange(12, [9, 6, 5, 1]))










