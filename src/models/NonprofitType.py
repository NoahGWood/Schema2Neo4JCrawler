from pydantic import BaseModel
from typing import Optional, Any

class NonprofitType(BaseModel):
    nonprofitStatus: Optional[Any] = None

