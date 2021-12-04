#Sabeen Fatima 
#Week1 
#Task 1 and Task 2 done

#Task 1: Greedy Exchange
def greedy_exchange(amount, denominations):
	coins=[0]*len(denominations) #initialisng coins array with 0 for  number of denominations
	i=0
	while( amount > 0 ):
		res= amount//denominations[i] # // sign is used for integer division
		if res>0 :
			coins[i]=res
		amount = amount - (res*(denominations[i]))
		i=i+1
	return coins #returning array/list of coins



#calling the function with different parameters
print("Task 1: Greedy Exchange ")
print (greedy_exchange(56, [20, 10, 5, 1]))
print(greedy_exchange(350, [100, 50, 10, 5, 2, 1]))
print(greedy_exchange(12, [9, 6, 5, 1]))

#Task2:
#get input and display the MINIMUM coins used
def brute_force_coin_exchange(amount, denominations):
    coins=[0]*len(denominations) #initialisng coins array with number of denominations
    i=0
    #find the minimum in the list and subtract amount by it 
    minimum_coin= min(denominations)
    index_min_coin = denominations.index(minimum_coin)  #index of min coin found 
    amount=amount-minimum_coin #now amount-minimum_coin
    coins[index_min_coin] = minimum_coin #place minimum_coin in index of minimum_coin 
    while( amount > 0 ):
        res= amount//denominations[i]   # //sign is used for integer division
        rem = amount % denominations[i] # check if remainder is 0
        if rem == 0 :
            coins[i]=res
            amount = amount - (res*(denominations[i]))
        i=i+1
    return coins


print("\nTask 2: Brute Force Coin Exchange ")
total_amount =int (input("Enter the Amount please : "))
print(total_amount)
numb = input("Enter number of coins/denominations")
numb= int(numb) #store in integer
#now get input and store in the list of coins
coins_list=[]
# iterating till the range 0 to numb
for i in range(0, numb):
    coins = int(input())
    coins_list.append(coins) # appending list
print("Your Input List is: ")
print (coins_list)
print("Output of Minimum Coins")
print (brute_force_coin_exchange(total_amount, coins_list))
print("\nRunning Test Case")
print (brute_force_coin_exchange(15, [10, 7, 6, 1]))
