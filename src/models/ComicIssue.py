from pydantic import BaseModel
from models.PublicationIssue import PublicationIssue

from typing import Optional, Any

class ComicIssue(PublicationIssue):
    artist: Optional[Any] = None
    colorist: Optional[Any] = None
    inker: Optional[Any] = None
    letterer: Optional[Any] = None
    penciler: Optional[Any] = None
    variantCover: Optional[Any] = None

