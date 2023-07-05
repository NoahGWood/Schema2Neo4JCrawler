from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class SoftwareSourceCode(CreativeWork):
    codeRepository: Optional[Any] = None
    codeSampleType: Optional[Any] = None
    programmingLanguage: Optional[Any] = None
    runtimePlatform: Optional[Any] = None
    targetProduct: Optional[Any] = None

