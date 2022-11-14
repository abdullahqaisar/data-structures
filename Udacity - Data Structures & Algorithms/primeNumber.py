
def get_prime(position):

    if position = 1:
        return position
    else:
        return (get_fib(position - 1) + get_fib(position - 2))

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
