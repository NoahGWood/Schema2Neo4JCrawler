from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Book(CreativeWork):
    abridged: Optional[Any] = None
    bookEdition: Optional[Any] = None
    bookFormat: Optional[Any] = None
    illustrator: Optional[Any] = None
    isbn: Optional[Any] = None
    numberOfPages: Optional[Any] = None

