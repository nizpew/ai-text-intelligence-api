from fastapi import FastAPI

from app.schemas import (
    TextRequest,
    SentimentResponse,
    ClassificationResponse,
    SummaryResponse,
)

from app.services.sentiment import analyze_sentiment
from app.services.classifier import classify_text
from app.services.summarizer import summarize_text

app = FastAPI(
    title="AI Text Intelligence API",
    description="API de análise de texto com NLP (sentimento, classificação e resumo)",
    version="1.0.0",
)


@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(request: TextRequest):
    """
    Analisa o sentimento do texto enviado.
    Retorna o sentimento (positivo, negativo ou neutro) e um score.
    """
    return analyze_sentiment(request.text)


@app.post("/classify", response_model=ClassificationResponse)
def classify(request: TextRequest):
    """
    Classifica o texto em categorias simples.
    """
    return {"label": classify_text(request.text)}


@app.post("/summarize", response_model=SummaryResponse)
def summarize(request: TextRequest):
    """
    Retorna um resumo simples do texto enviado.
    """
    return {"summary": summarize_text(request.text)}
