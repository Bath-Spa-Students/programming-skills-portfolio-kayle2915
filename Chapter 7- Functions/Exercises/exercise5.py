# Function to describe a city
def describe_city(city, country="USA"):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Calling the function for different cities
describe_city("New York")
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")