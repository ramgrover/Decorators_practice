class UnauthorizedError(Exception):
    pass

#Defines a custom exception class UnauthorizedError that inherits from the built-in Exception class.
#This will be used to raise an exception when unauthorized access is detected.

def authorize(username, password):
#Defines the outer function authorize that takes username and password as arguments. 
#This function returns the actual decorator.
    def decorator(func):
        # Define the predefined credentials
        predefined_username = "admin"
        predefined_password = "secretpassword"
        
        def wrapper(*args, **kwargs):
            # Check if provided credentials match predefined values
            if username == predefined_username and password == predefined_password:
                # If credentials are correct, execute the original function
                return func(*args, **kwargs)
            else:
                # If credentials are incorrect, raise UnauthorizedError
                raise UnauthorizedError("Unauthorized access. Please provide valid credentials.")
        
        return wrapper
    
    return decorator

# Example usage:

@authorize(username="admin", password="secretpassword")
#Decorates the sensitive_operation function with the provided username and password.
def sensitive_operation():
    print("Executing sensitive operation.")

try:
    # Correct credentials
    sensitive_operation()
except UnauthorizedError as e:
    print(e)

try:
    # Incorrect credentials
    unauthorized_function = authorize(username="user", password="wrongpassword")(sensitive_operation)
    unauthorized_function()
except UnauthorizedError as e:
    print(e)
