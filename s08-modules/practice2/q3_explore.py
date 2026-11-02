import random

print([name for name in dir(random) if name.islower() and not name.startswith("_")][:8])
print(random.choice.__doc__.splitlines()[0])
