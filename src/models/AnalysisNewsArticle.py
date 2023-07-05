from pydantic import BaseModel
from models.Article import Article

from typing import Optional, Any

class AnalysisNewsArticle(Article):
    dateline: Optional[Any] = None
    printColumn: Optional[Any] = None
    printEdition: Optional[Any] = None
    printPage: Optional[Any] = None
    printSection: Optional[Any] = None

