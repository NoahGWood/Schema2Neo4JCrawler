from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalCondition(MedicalEntity):
    associatedAnatomy: Optional[Any] = None
    differentialDiagnosis: Optional[Any] = None
    drug: Optional[Any] = None
    epidemiology: Optional[Any] = None
    expectedPrognosis: Optional[Any] = None
    naturalProgression: Optional[Any] = None
    pathophysiology: Optional[Any] = None
    possibleComplication: Optional[Any] = None
    possibleTreatment: Optional[Any] = None
    primaryPrevention: Optional[Any] = None
    riskFactor: Optional[Any] = None
    secondaryPrevention: Optional[Any] = None
    signOrSymptom: Optional[Any] = None
    stage: Optional[Any] = None
    status: Optional[Any] = None
    typicalTest: Optional[Any] = None

