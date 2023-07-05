from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DataFeedItem(Thing):
    dateCreated: Optional[Any] = None
    dateDeleted: Optional[Any] = None
    dateModified: Optional[Any] = None
    item: Optional[Any] = None

