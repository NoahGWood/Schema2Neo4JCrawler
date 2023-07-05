from pydantic import BaseModel
from models.WebPage import WebPage

from typing import Optional, Any

class MedicalWebPage(WebPage):
    medicalAudience: Optional[Any] = None

