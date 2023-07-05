from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class TouristAttraction(Place):
    availableLanguage: Optional[Any] = None
    touristType: Optional[Any] = None

