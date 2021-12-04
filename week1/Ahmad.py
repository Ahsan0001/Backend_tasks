def greedy_exchange(amount,deno):
    deno.sort(reverse=True)
    x = 1
    sum = 0
    i = 0
    j = 0
    deno2 = []
    while x==1:
        while sum<=amount:
            if deno[i]<amount:
                sum = sum + deno[i]
                if sum<=amount:
                    j = j + 1
                else:
                    break

        deno2.append(j)
        j = 0
        sum = sum-deno[i]
        i = i+1
        if sum>=amount:
            x = 0

    print("coins = ",end="")
    print(deno2)


greedy_exchange(12,[9,6,5,1])
