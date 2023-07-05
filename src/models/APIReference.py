from pydantic import BaseModel
from models.TechArticle import TechArticle

from typing import Optional, Any

class APIReference(TechArticle):
    assemblyVersion: Optional[Any] = None
    executableLibraryName: Optional[Any] = None
    programmingModel: Optional[Any] = None
    targetPlatform: Optional[Any] = None

