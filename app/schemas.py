from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    score: int

class ClassificationResponse(BaseModel):
    label: str

class SummaryResponse(BaseModel):
    summary: str