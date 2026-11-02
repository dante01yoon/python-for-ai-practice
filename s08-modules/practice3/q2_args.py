import sys

print("Arguments:", sys.argv)
if len(sys.argv) > 1:
    city = " ".join(sys.argv[1:])
else:
    city = "Chicago"
print(f"Weather report for {city}")
