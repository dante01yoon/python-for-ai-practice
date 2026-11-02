# Mini project: US unit converter
fahrenheit = float(input("Temperature in °F: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius:.1f}°C")

miles = float(input("Distance in miles: "))
print(f"{miles} miles is {miles * 1.609:.1f} km")

pounds = float(input("Weight in lb: "))
print(f"{pounds} lb is {pounds * 0.4536:.1f} kg")
