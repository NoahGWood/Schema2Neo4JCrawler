from pydantic import BaseModel
from models.MedicalTest import MedicalTest

from typing import Optional, Any

class PathologyTest(MedicalTest):
    tissueSample: Optional[Any] = None

