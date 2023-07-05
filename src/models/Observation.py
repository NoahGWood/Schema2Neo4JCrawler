from pydantic import BaseModel
from models.QuantitativeValue import QuantitativeValue

from typing import Optional, Any

class Observation(QuantitativeValue):
    marginOfError: Optional[Any] = None
    measuredProperty: Optional[Any] = None
    measurementDenominator: Optional[Any] = None
    measurementMethod: Optional[Any] = None
    measurementQualifier: Optional[Any] = None
    measurementTechnique: Optional[Any] = None
    observationAbout: Optional[Any] = None
    observationDate: Optional[Any] = None
    observationPeriod: Optional[Any] = None
    variableMeasured: Optional[Any] = None

