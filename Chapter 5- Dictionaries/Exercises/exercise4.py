# rivers

rivers = {
    'nile river' : 'egypt',
    'the amazon river' : 'south america',
    'the ganges river' : 'india , bangladesh',
    'the mississippi' : 'North america'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# rivers
print("\nRivers:")
for river in rivers.keys():
    print(river)

# country
print("\nCountries:")
for country in rivers.values():
    print(country)
