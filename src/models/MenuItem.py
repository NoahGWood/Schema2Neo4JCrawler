from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class MenuItem(Thing):
    menuAddOn: Optional[Any] = None
    nutrition: Optional[Any] = None
    offers: Optional[Any] = None
    suitableForDiet: Optional[Any] = None

