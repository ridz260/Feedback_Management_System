from pydantic import BaseModel
from typing import List, Optional

class Survey(BaseModel):
    title: str
    questions: List[dict]
    start_date: str
    end_date: str

class Response(BaseModel):
    survey_id: str
    answers: List[dict]