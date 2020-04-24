"""Mathematical approach to solve problem 1."""

def sum_divisible_by(num, upper):
    """Return sum of all divisible number by 'num' below 'upper'"""
    return num * (upper // num) * (upper // num + 1) // 2

def multiples_3_or_5(upper):
    """Return the sum of all the multiples of 3 or 5 below upper"""
    return sum_divisible_by(3, upper) + sum_divisible_by(5, upper) - sum_divisible_by(15, upper)

if __name__ == "__main__":
    import time
    start = time.time()
    print("Result: {}".format(multiples_3_or_5(1000)))
    end = time.time()
    print("Mathematical solution time: {}".format(end - start))