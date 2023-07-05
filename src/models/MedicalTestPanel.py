from pydantic import BaseModel
from models.MedicalTest import MedicalTest

from typing import Optional, Any

class MedicalTestPanel(MedicalTest):
    subTest: Optional[Any] = None

