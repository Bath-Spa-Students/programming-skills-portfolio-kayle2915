# Function to make a shirt with default values
def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"The shirt is size {size} and the message on it is: '{message}'")

# Making a large shirt with default message
make_shirt()

# Making a medium shirt with default message
make_shirt("medium")

# Making a shirt of any size with a different message
make_shirt("small", "Hello World!")