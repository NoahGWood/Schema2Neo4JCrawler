from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class NutritionInformation(Thing):
    calories: Optional[Any] = None
    carbohydrateContent: Optional[Any] = None
    cholesterolContent: Optional[Any] = None
    fatContent: Optional[Any] = None
    fiberContent: Optional[Any] = None
    proteinContent: Optional[Any] = None
    saturatedFatContent: Optional[Any] = None
    servingSize: Optional[Any] = None
    sodiumContent: Optional[Any] = None
    sugarContent: Optional[Any] = None
    transFatContent: Optional[Any] = None
    unsaturatedFatContent: Optional[Any] = None

