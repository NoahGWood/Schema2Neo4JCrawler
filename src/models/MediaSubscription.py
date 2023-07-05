from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class MediaSubscription(Thing):
    authenticator: Optional[Any] = None
    expectsAcceptanceOf: Optional[Any] = None

