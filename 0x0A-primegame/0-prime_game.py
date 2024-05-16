#!/usr/bin/python3
"""A Prime game module.
"""


def isWinner(x, nums):
    """ It Determines the winner of a prime game session with `x` rounds
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate  maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for m in range(i + i, n + 1, i):
            primes[m - 1] = False
    # filter the number of primes less than n 
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
