import json
from pathlib import Path

path = Path("settings.json")
if path.exists():
    settings = json.loads(path.read_text())
else:
    settings = {"theme": "dark", "font_size": 14, "visits": 0}

settings["visits"] += 1
path.write_text(json.dumps(settings, indent=2))
print(f"Visit number {settings['visits']}, theme {settings['theme']}")
