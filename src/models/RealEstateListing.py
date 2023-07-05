from pydantic import BaseModel
from models.WebPage import WebPage

from typing import Optional, Any

class RealEstateListing(WebPage):
    datePosted: Optional[Any] = None
    leaseLength: Optional[Any] = None

