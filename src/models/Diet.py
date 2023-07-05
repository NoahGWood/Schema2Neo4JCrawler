from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Diet(CreativeWork):
    dietFeatures: Optional[Any] = None
    endorsers: Optional[Any] = None
    expertConsiderations: Optional[Any] = None
    physiologicalBenefits: Optional[Any] = None
    risks: Optional[Any] = None

