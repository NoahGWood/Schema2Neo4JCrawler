from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class Airline(Organization):
    boardingPolicy: Optional[Any] = None
    iataCode: Optional[Any] = None

