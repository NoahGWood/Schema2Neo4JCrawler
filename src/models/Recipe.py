from pydantic import BaseModel
from models.HowTo import HowTo

from typing import Optional, Any

class Recipe(HowTo):
    cookTime: Optional[Any] = None
    cookingMethod: Optional[Any] = None
    nutrition: Optional[Any] = None
    recipeCategory: Optional[Any] = None
    recipeCuisine: Optional[Any] = None
    recipeIngredient: Optional[Any] = None
    recipeInstructions: Optional[Any] = None
    recipeYield: Optional[Any] = None
    suitableForDiet: Optional[Any] = None

