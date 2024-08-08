#!/usr/bin/python3
'''Prime Game module'''


def isWinner(x, nums):
    '''
    Determines winner of set of prime number removal games.

    Args:
        x (int): Number of rounds.
        nums (list of int): list of integers where each integer n denotes
        set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: Name of player who won most rounds (either "Ben"
        or "Maria").
        None: If winner cannot be determined.

    Raises:
        None.
    '''
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Initialize scores and array of possible prime numbers
    ben = 0
    maria = 0
    # create list 'a' of length sorted(nums)[-1] + 1 with all elements
    # initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # First two elements of the list, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0
    # use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for j in range(2, len(a)):
        rm_multiples(a, j)
    # play each round of game
    for j in nums:
        # If sum of prime numbers in set is even, Ben wins
        if sum(a[0:j + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine winner of game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    '''
    removes multiples of prime number from array of possible prime
    numbers.

    Args:
        ls (list of int): Array of possible prime numbers.
        x (int): Prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    '''
    # This loop iterates over multiples of prime number and marks them as
    # non-prime by setting their corresponding value to 0 in input
    # list ls. Starting from 2, it sets every multiple of x up to 
    # length of ls to 0. If index j * x is out of range for list ls,
    # try block will raise an IndexError exception, and loop will
    # terminate using break statement.
    for j in range(2, len(ls)):
        try:
            ls[j * x] = 0
        except (ValueError, IndexError):
            break
























































