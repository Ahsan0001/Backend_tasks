# Task 1: Greedy Exchange
def greedy_exchange(amount, denominations):
    """
    >>> greedy_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> greedy_exchange(350, [100, 50, 10, 5, 2, 1])
    [3, 1, 0, 0, 0, 0]
    >>> greedy_exchange(12, [9, 6, 5, 1])
    [1, 0, 0, 3]
    """
    # Create a list to store the number of coins
    # values already in sorted order
    # else sort the list

    coins = [0] * len(denominations)
    # Loop through the denominations list
    for i in range(len(denominations)):
        # If the amount is greater than the denomination
        if amount >= denominations[i]:
            # Add the number of coins to the list
            coins[i] = amount // denominations[i]
            # Subtract the number of coins from the amount
            amount -= coins[i] * denominations[i]
    return coins


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
