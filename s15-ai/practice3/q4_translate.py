import httpx

URL = "http://localhost:11434/api/chat"


def translate(text: str, language: str) -> str:
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": f"Translate the user's text into {language}. Reply with the translation only."},
            {"role": "user", "content": text},
        ],
        "stream": False,
        "options": {"temperature": 0},
    }
    return httpx.post(URL, json=payload, timeout=120).json()["message"]["content"].strip()


for language in ["Spanish", "French", "German"]:
    print(language, "->", translate("Where is the nearest coffee shop?", language))
