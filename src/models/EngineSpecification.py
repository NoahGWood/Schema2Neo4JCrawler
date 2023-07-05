from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class EngineSpecification(Thing):
    engineDisplacement: Optional[Any] = None
    enginePower: Optional[Any] = None
    engineType: Optional[Any] = None
    fuelType: Optional[Any] = None
    torque: Optional[Any] = None

