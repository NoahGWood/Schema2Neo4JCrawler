from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class ReportedDoseSchedule(MedicalEntity):
    doseUnit: Optional[Any] = None
    doseValue: Optional[Any] = None
    frequency: Optional[Any] = None
    targetPopulation: Optional[Any] = None

