def greedy_exchange(amount, denominations):
    ans = [0]*len(denominations)
    i = 0
    while(amount):
        while (amount >= denominations[i]):
            amount -= denominations[i]
            ans[i] += 1

        i += 1

    return ans
  
# Driver Code
change = greedy_exchange(56, [20, 10, 5, 1])
print (change)

print (greedy_exchange(350, [100, 50, 10, 5, 2, 1]))
print (greedy_exchange(12, [9, 6, 5, 1]))
