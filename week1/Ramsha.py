def greedy_exchange(amount, denominations):
  size = int(len(denominations))
  temp_size=int(len(denominations))
  numbers=[0] * size
  numbers2=[0] * size
  i = 0
  temp_denomination=denominations
  denominations.sort(reverse=True)

  while(amount>0):
    if(denominations[i] > amount):
      numbers[i]=numbers[i]+0
      i = i+1
      
    else:
     # print(denominations[i])
      numbers[i]=numbers[i]+1
      amount = amount-denominations[i];
  max=0
  i = 0
  index=0;
  while(int(temp_size)>0):
       while(size>0):
           #print(size)
           if(denominations[i]>max):
                pos=i
                max=denominations[i]
           i=i+1
           size=size-1
       numbers2[pos]=numbers[index]
       index=index+1
       i=index
       #print("\n")
       temp_size=temp_size-1
       max=0
       size=temp_size

  #print("\n")
  #print(numbers2)
  return numbers2


if __name__ == '__main__':
  numbers=greedy_exchange(56,[20,10,5,1])
  print("OUTPUT IS: ")
  print(numbers)
  numbers=greedy_exchange(350,[100,50,10,5,2,1])
 
  print(numbers)
  numbers=greedy_exchange(12,[9,6,5,1])
  print(numbers)
  numbers=greedy_exchange(6, [1, 3, 4] )
  print(numbers)
