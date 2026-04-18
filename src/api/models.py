from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

class GeneticRisk(BaseModel):
    condition: str
    risk_level: RiskLevel
    population_risk: float
    patient_risk: float
    relative_risk: float
    confidence: float = Field(ge=0.0, le=1.0)
    associated_genes: List[str]
    clinical_implications: str
    recommendations: List[str]
    references: Optional[List[str]] = None

class CarrierStatus(BaseModel):
    condition: str
    inheritance: str
    carrier_status: str
    gene: str
    variant: Optional[str]
    carrier_frequency: Optional[str]
    implications: str
    recommendations: List[str]

class AncestryRegion(BaseModel):
    region: str
    percentage: float = Field(ge=0.0, le=100.0)
    subregions: List[str]

class DrugResponse(BaseModel):
    drug: str
    gene: str
    phenotype: str
    implications: str
    recommendation: str

class WellnessTrait(BaseModel):
    trait: str
    result: str
    implications: str
    genes: List[str]

class GeneticReport(BaseModel):
    metadata: Dict[str, Any]
    patient_info: Dict[str, Any]
    genetic_risk_assessment: Dict[str, Any]
    carrier_status: Dict[str, Any]
    ancestry_analysis: Dict[str, Any]
    pharmacogenomics: Dict[str, Any]
    wellness_traits: Dict[str, Any]
    raw_data_summary: Dict[str, Any]
    interpretation_notes: List[str]
    disclaimers: List[str]

class PDFProcessingRequest(BaseModel):
    file_name: str
    file_size: int
    upload_timestamp: datetime

class PDFProcessingResponse(BaseModel):
    report_id: str
    status: str
    extracted_text: Optional[str]
    structured_data: Optional[GeneticReport]
    processing_time: float
    errors: List[str] = []

class ChatMessage(BaseModel):
    role: str
    content: str
    timestamp: datetime

class Conversation(BaseModel):
    report_id: str
    messages: List[ChatMessage]
    summary: Optional[str]

class Recommendation(BaseModel):
    text: str
    category: str
    priority: str
    evidence_level: str
    actionable_steps: List[str]