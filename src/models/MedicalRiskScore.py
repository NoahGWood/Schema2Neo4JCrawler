from pydantic import BaseModel
from models.MedicalRiskEstimator import MedicalRiskEstimator

from typing import Optional, Any

class MedicalRiskScore(MedicalRiskEstimator):
    algorithm: Optional[Any] = None

