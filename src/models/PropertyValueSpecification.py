from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class PropertyValueSpecification(Thing):
    defaultValue: Optional[Any] = None
    maxValue: Optional[Any] = None
    minValue: Optional[Any] = None
    multipleValues: Optional[Any] = None
    readonlyValue: Optional[Any] = None
    stepValue: Optional[Any] = None
    valueMaxLength: Optional[Any] = None
    valueMinLength: Optional[Any] = None
    valueName: Optional[Any] = None
    valuePattern: Optional[Any] = None
    valueRequired: Optional[Any] = None

