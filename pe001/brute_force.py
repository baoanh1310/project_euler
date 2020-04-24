"""Solution for Problem 1"""

def multiples_3_or_5(upper):
    """Return the sum of all the multiples of 3 or 5 below upper"""
    return sum([number for number in range(3, upper) if not number % 3 or not number % 5])

if __name__ == "__main__":
    import time
    start = time.time()
    print("Result: {}".format(multiples_3_or_5(1000)))
    end = time.time()
    print("Bruteforce solution time: {}".format(end - start))
