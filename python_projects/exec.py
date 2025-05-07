def factorial(n):
    if n == 0:
        return 1
    else:
        return(n * factorial(n - 1))


def fact_one_line(n):
    return n * fact_one_line(n - 1) if n != 0 else 1
