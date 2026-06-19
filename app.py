from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import CourseRecommender
import os

app = FastAPI(title="CourseFinder")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'courses.csv')

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

recommender = CourseRecommender(CSV_PATH)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"active": "home"})


@app.get("/recommend", response_class=HTMLResponse)
async def recommend_page(request: Request):
    return templates.TemplateResponse(request, "recommend.html", {"active": "recommend"})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request, "about.html", {"active": "about"})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"active": "contact"})


@app.get("/api/courses")
async def get_courses():
    return JSONResponse({"courses": recommender.get_courses()})


class RecommendRequest(BaseModel):
    course_name: str

@app.post("/api/recommend")
async def recommend(req: RecommendRequest):
    return JSONResponse({"recommendations": recommender.recommend(req.course_name)})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
