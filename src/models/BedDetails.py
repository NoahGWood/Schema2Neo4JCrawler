from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class BedDetails(Thing):
    numberOfBeds: Optional[Any] = None
    typeOfBed: Optional[Any] = None

