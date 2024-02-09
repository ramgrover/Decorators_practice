#Implement a memoization decorator using closures. The decorator should cache the results of a 
#function for particular arguments and return the cached result when the function is called with 
#those arguments again, instead of recomputing it.

def memoize(func):
    cache = {} #It's a dictionary names cache which is initialized, inside it dictionary will be used
    #to store the results of function calls for specific arguments.

    def wrapper(*args):
#Here, an inner function called wrapper is defined within the memoize function. It takes any number 
#of arguments (*args), allowing it to work with functions that accept different sets of arguments.
        if args in cache:
# If the result for these arguments is already in the cache, return it
            return cache[args]
        else:
# Otherwise, compute the result, cache it, and return it
            result = func(*args)
            cache[args] = result
#The result is then cached in the cache dictionary, associating it with the specific arguments.
            return result

    return wrapper
#The wrapper function is returned from the memoize function. This effectively replaces the 
#original function with this wrapped version.

# Example usage:
@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the decorated function
result = factorial(5)
print(result)
