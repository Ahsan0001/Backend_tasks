def greedy_exchange(amount, denominations):
    ret = []
    temp = amount
    flag = False
    denominations.sort(reverse=True)

    for den in denominations:
        i = 0
        while temp >= den:
            i += 1
            temp -= den

        ret.append(i)

    return ret


val = greedy_exchange(56, [20, 10, 5, 1])
print(val)

val = greedy_exchange(350, [100, 50, 10, 5, 2, 1])
print(val)

val =  greedy_exchange(12, [9, 6, 5, 1])
print(val)