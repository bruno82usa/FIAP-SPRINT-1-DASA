from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
import json
from datetime import datetime

app = FastAPI(
    title="DASA Genera AI Assistant API",
    description="API for processing genetic reports and providing AI-powered insights",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str

class UploadResponse(BaseModel):
    report_id: str
    status: str
    message: str
    estimated_processing_time: int

class QuestionRequest(BaseModel):
    report_id: str
    question: str

class QuestionResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[str]
    disclaimer: str

class RecommendationRequest(BaseModel):
    report_id: str

class RecommendationResponse(BaseModel):
    recommendations: List[str]
    categories: List[str]
    priority: str

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to DASA Genera AI Assistant API",
        "endpoints": {
            "health": "/health",
            "upload": "/upload",
            "ask": "/ask",
            "recommendations": "/recommendations/{report_id}"
        }
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )

@app.post("/upload", response_model=UploadResponse, tags=["Reports"])
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    report_id = str(uuid.uuid4())[:8]
    
    return UploadResponse(
        report_id=report_id,
        status="received",
        message="PDF received and queued for processing",
        estimated_processing_time=30
    )

@app.post("/ask", response_model=QuestionResponse, tags=["AI"])
async def ask_question(request: QuestionRequest):
    sample_answers = {
        "What is my risk for diabetes?": "Based on your genetic profile, you have a moderate increased risk for Type 2 Diabetes (approximately 25% lifetime risk compared to 10% population average). This is associated with variants in TCF7L2 and PPARG genes.",
        "What does being a carrier mean?": "Being a carrier means you have one copy of a gene variant for an autosomal recessive condition. You typically don't show symptoms but could pass it to your children if your partner is also a carrier.",
        "What are my main genetic risks?": "Your primary genetic risks include: 1) Type 2 Diabetes (moderate risk), 2) Coronary Artery Disease (slightly increased risk), 3) Carrier status for Cystic Fibrosis.",
        "What should I do based on my results?": "Based on your genetic profile, consider: 1) Annual glucose monitoring, 2) Heart-healthy diet, 3) Regular exercise, 4) Discuss carrier status with partner and consider genetic counseling."
    }
    
    answer = sample_answers.get(
        request.question, 
        "I can help answer questions about your genetic report. Please ask about specific risks, carrier status, or recommendations based on your results."
    )
    
    return QuestionResponse(
        answer=answer,
        confidence=0.85,
        sources=["Genetic risk databases", "Clinical guidelines"],
        disclaimer="This information is for educational purposes only. Consult with a healthcare professional for medical advice."
    )

@app.get("/recommendations/{report_id}", response_model=RecommendationResponse, tags=["Recommendations"])
async def get_recommendations(report_id: str):
    return RecommendationResponse(
        recommendations=[
            "Schedule annual fasting glucose test",
            "Maintain Mediterranean-style diet rich in vegetables and healthy fats",
            "Engage in 150 minutes of moderate exercise weekly",
            "Monitor blood pressure regularly",
            "Consider genetic counseling for family planning"
        ],
        categories=["Metabolic Health", "Cardiovascular", "Lifestyle", "Prevention"],
        priority="medium"
    )

@app.get("/reports/{report_id}/summary", tags=["Reports"])
async def get_report_summary(report_id: str):
    return {
        "report_id": report_id,
        "status": "processed",
        "summary": {
            "risk_factors": 3,
            "carrier_status": 1,
            "ancestry_regions": 5,
            "wellness_traits": 4
        },
        "processed_at": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8789)