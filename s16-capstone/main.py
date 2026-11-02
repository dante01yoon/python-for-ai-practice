from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from forecast import CITIES, Hour, fetch_hours
from summary import summarize

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/api/hours")
def hours(city: str = "New York") -> list[Hour]:
    return fetch_hours(city)


@app.get("/", response_class=HTMLResponse)
def home(request: Request, city: str = "New York") -> HTMLResponse:
    hours = fetch_hours(city)
    warmest = max(hours, key=lambda h: h.temp)
    return templates.TemplateResponse(
        request, "page.html", {"city": city, "cities": CITIES, "hours": hours, "warmest": warmest, "summary": summarize(city, hours)}
    )
