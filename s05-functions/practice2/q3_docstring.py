def miles_to_km(miles):
    """Convert miles to kilometers. One mile is exactly 1.609344 km."""
    return miles * 1.609344


print(miles_to_km.__doc__)
print(round(miles_to_km(26.2), 1))
