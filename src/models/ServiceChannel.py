from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ServiceChannel(Thing):
    availableLanguage: Optional[Any] = None
    processingTime: Optional[Any] = None
    providesService: Optional[Any] = None
    serviceLocation: Optional[Any] = None
    servicePhone: Optional[Any] = None
    servicePostalAddress: Optional[Any] = None
    serviceSmsNumber: Optional[Any] = None
    serviceUrl: Optional[Any] = None

