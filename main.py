from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["feedback_db"]

# Pydantic models
class Survey(BaseModel):
    title: str
    questions: List[str]
    start_date: str
    end_date: str

class Response(BaseModel):
    survey_id: str
    answers: List[str]

# Serve static files from the 'frontend' directory
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Feedback Management System!"}

# Create a new survey
@app.post("/surveys/")
async def create_survey(survey: Survey):
    survey_dict = survey.dict()
    db.surveys.insert_one(survey_dict)
    return {"message": "Survey created successfully!"}

# Submit a response to a survey
@app.post("/responses/")
async def submit_response(response: Response):
    response_dict = response.dict()
    db.responses.insert_one(response_dict)
    return {"message": "Response submitted successfully!"}

# Get all surveys
@app.get("/surveys/")
async def get_surveys():
    surveys = list(db.surveys.find())
    return surveys

# Get responses for a specific survey
@app.get("/responses/{survey_id}")
async def get_responses(survey_id: str):
    responses = list(db.responses.find({"survey_id": survey_id}))
    if not responses:
        raise HTTPException(status_code=404, detail="No responses found for this survey.")
    return responses
