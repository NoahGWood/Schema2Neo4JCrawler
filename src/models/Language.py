from pydantic import BaseModel
from typing import Optional, Any

class Language(BaseModel):
    additionalType: Optional[Any] = None
    alternateName: Optional[Any] = None
    description: Optional[Any] = None
    disambiguatingDescription: Optional[Any] = None
    identifier: Optional[Any] = None
    image: Optional[Any] = None
    mainEntityOfPage: Optional[Any] = None
    name: Optional[Any] = None
    potentialAction: Optional[Any] = None
    sameAs: Optional[Any] = None
    subjectOf: Optional[Any] = None
    url: Optional[Any] = None

