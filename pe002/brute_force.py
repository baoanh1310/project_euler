"""Bruteforce approach to solve problem 2."""
def sum_even_fibo(upper):
    """Return sum of all even-valued terms in Fibonacci sequence below upper+1"""
    result = 0
    x = 1
    y = 2
    while x <= upper:
        if x % 2 == 0:
            result += x
        x, y = y, x + y
    return result

if __name__ == "__main__":
    import time
    start = time.time()
    print("Result: {}".format(sum_even_fibo(4000000)))
    end = time.time()
    print("Bruteforce solution time: {}".format(end - start))