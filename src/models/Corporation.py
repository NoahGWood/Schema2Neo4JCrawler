from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class Corporation(Organization):
    tickerSymbol: Optional[Any] = None

