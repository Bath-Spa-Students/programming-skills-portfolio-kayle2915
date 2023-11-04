# Function to make a shirt
def make_shirt(size, message):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"The shirt is size {size} and the message on it is: '{message}'")

# Using positional arguments
make_shirt("M", "python is easy")

# Using keyword arguments
make_shirt(size="L", message="Hello World!")