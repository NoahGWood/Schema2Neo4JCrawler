from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class FastFoodRestaurant(LocalBusiness):
    acceptsReservations: Optional[Any] = None
    hasMenu: Optional[Any] = None
    servesCuisine: Optional[Any] = None
    starRating: Optional[Any] = None

