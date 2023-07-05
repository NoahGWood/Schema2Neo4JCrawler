from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class DietarySupplement(Product):
    activeIngredient: Optional[Any] = None
    isProprietary: Optional[Any] = None
    legalStatus: Optional[Any] = None
    maximumIntake: Optional[Any] = None
    mechanismOfAction: Optional[Any] = None
    nonProprietaryName: Optional[Any] = None
    proprietaryName: Optional[Any] = None
    recommendedIntake: Optional[Any] = None
    safetyConsideration: Optional[Any] = None
    targetPopulation: Optional[Any] = None

