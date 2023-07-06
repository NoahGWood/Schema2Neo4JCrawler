from pydantic import BaseModel
from typing import Optional, Any

class BookFormatType(BaseModel):
    bookFormat: Optional[Any] = None

