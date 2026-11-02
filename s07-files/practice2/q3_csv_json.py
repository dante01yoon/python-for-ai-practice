import csv
import json

with open("parks.csv", "w", newline="") as f:
    f.write("park,state,established\nYellowstone,Wyoming,1872\nYosemite,California,1890\nAcadia,Maine,1916\n")

with open("parks.csv", newline="") as f:
    parks = list(csv.DictReader(f))
for park in parks:
    park["established"] = int(park["established"])

with open("parks.json", "w") as f:
    json.dump(parks, f, indent=2)
print(json.dumps(parks[0]))
