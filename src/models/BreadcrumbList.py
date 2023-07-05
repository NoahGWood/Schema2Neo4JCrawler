from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class BreadcrumbList(Thing):
    itemListElement: Optional[Any] = None
    itemListOrder: Optional[Any] = None
    numberOfItems: Optional[Any] = None

