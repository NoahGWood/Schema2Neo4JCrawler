from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class IndividualProduct(Product):
    serialNumber: Optional[Any] = None

