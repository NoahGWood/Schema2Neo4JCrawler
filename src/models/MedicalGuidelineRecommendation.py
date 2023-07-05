from pydantic import BaseModel
from models.MedicalGuideline import MedicalGuideline

from typing import Optional, Any

class MedicalGuidelineRecommendation(MedicalGuideline):
    recommendationStrength: Optional[Any] = None

