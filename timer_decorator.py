#Timer Decorator: Write a decorator function called timer that calculates the time taken for a 
#function to execute and prints the duration. It should be able to decorate any function and print 
#the time taken for execution.

import time #this line imports the time module which provides time related function in python.

def timer(func): #This line defines the timer decorator function. It takes a function (func) as its argument.
    def wrapper(*args, **kwargs):
#Here, we define an inner function called wrapper. This function takes any number of positional 
#and keyword arguments (*args and **kwargs). This allows the decorator to work with functions 
#that accept different sets of arguments.
        start_time = time.time()
#This line records the current time using time.time() just before the decorated function is called. 
#This will be the starting time for measuring the duration.
        result = func(*args, **kwargs)
#This line calls the original function (func) with the provided arguments and captures its result.
        end_time = time.time()
#This line records the current time again using time.time(). This will be the ending time for measuring the duration.
        duration = end_time - start_time
#Calculates the time taken for the function to execute by subtracting the start time from the end time.
        print(f"{func.__name__} took {duration:.4f} seconds to execute.")
        return result
    return wrapper
#returns wrapper function, replacing the original function with its wrapped function.

@timer
def ex_function():
    time.sleep(5)
    print("Function executed!")


ex_function()#calling the fucntion

