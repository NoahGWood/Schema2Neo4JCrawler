from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class WarrantyPromise(Thing):
    durationOfWarranty: Optional[Any] = None
    warrantyScope: Optional[Any] = None

