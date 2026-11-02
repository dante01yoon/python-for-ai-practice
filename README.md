# The Ultimate Python Master Course for AI — Practice Code

Code for every section of the free YouTube course **The Ultimate Python Master Course for AI** by Dante Yoon ([@danteyoon](https://www.youtube.com/@danteyoon)).

Each folder matches a section of the video. `practice*` folders hold the challenges and their solutions.

| Folder | Section |
|---|---|
| `s01-setup` | Set Up Your Computer |
| `s02-values` | Values & Variables |
| `s03-collections` | Collections |
| `s04-control-flow` | Control Flow |
| `s05-functions` | Functions |
| `s06-errors` | Errors & Debugging |
| `s07-files` | Files & Data |
| `s08-modules` | Modules, Packages & uv |
| `s09-classes` | Classes & Objects |
| `s10-pythonic` | Pythonic Code |
| `s11-quality` | Type Hints & Code Quality |
| `s12-testing` | Testing with pytest |
| `s13-concurrency` | Concurrency & Coroutines |
| `s14-automation` | Automate Everyday Tasks |
| `s15-ai` | Python for AI (local LLM with Ollama) |
| `s16-capstone` | Capstone: A Weather Web App (FastAPI) |

## Run it

Install [uv](https://docs.astral.sh/uv/), then from any section folder:

```bash
uv run python <file>.py
```

Section 15 uses a local model through [Ollama](https://ollama.com) (`ollama pull llama3.2`), so no API key is needed.
