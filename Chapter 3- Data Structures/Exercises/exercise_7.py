# Create a list places i'd like to visit 
places = [ "machu picchu ,Peru", "The Grand Canyon,Arizona", "Rome,Italy", "Maui,Hawaii","Masai Mara,Kenya"]

# Print the list in its original order
print("Original order:")
print(places)

# places in alphabetical order
print("\nAlphabetical order:")
print(sorted(places))

# Show that the list still in orginal order
print("\nOriginal order (still):")
print(places)

# Use sorted() to print the list in reverse alphabetical order without changing the order of the original list
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Show that the original list is still in its original order
print("\nOriginal order (still again):")
print(places)

# Use reverse() to change the order of your list
places.reverse()
print("\nReversed order:")
print(places)

# Use reverse() to change the order of your list again
places.reverse()
print("\nBack to original order:")
print(places)

# Use sort() to change your list so it's stored in alphabetical order
places.sort()
print("\nSorted in alphabetical order:")
print(places)

# Use sort() to change your list so it's stored in reverse alphabetical order
places.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places)