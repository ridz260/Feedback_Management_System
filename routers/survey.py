from fastapi import APIRouter, HTTPException
from models import Survey, Response
from database import db

router = APIRouter()

@router.post("/surveys/")
async def create_survey(survey: Survey):
    survey_dict = survey.dict()
    db.surveys.insert_one(survey_dict)
    return {"message": "Survey created successfully"}

@router.get("/surveys/{survey_id}")
async def get_survey(survey_id: str):
    survey = db.surveys.find_one({"_id": survey_id})
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@router.post("/responses/")
async def submit_response(response: Response):
    response_dict = response.dict()
    db.responses.insert_one(response_dict)
    return {"message": "Response submitted successfully"}