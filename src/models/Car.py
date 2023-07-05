from pydantic import BaseModel
from models.Vehicle import Vehicle

from typing import Optional, Any

class Car(Vehicle):
    acrissCode: Optional[Any] = None
    roofLoad: Optional[Any] = None

