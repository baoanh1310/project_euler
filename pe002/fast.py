"""Mathematical approach to solve problem 2."""

def sum_even_fibo(upper):
    """
    Return sum of all even-valued terms in Fibonacci sequence below upper+1
    Fi(n) = 4 * Fi(n-3) + Fi(n-6)
    Fi: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    x = 2
    y = 8
    result = 0
    while x <= upper:
        result += x
        x, y = y, 4 * y + x
    return result

if __name__ == "__main__":
    import time
    start = time.time()
    print("Result: {}".format(sum_even_fibo(4000000)))
    end = time.time()
    print("Fast solution time: {}".format(end - start))
