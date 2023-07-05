from pydantic import BaseModel
from models.Article import Article

from typing import Optional, Any

class Report(Article):
    reportNumber: Optional[Any] = None

