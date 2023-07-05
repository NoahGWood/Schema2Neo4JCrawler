from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Thesis(CreativeWork):
    inSupportOf: Optional[Any] = None

