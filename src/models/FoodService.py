from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class FoodService(Thing):
    aggregateRating: Optional[Any] = None
    areaServed: Optional[Any] = None
    audience: Optional[Any] = None
    availableChannel: Optional[Any] = None
    award: Optional[Any] = None
    brand: Optional[Any] = None
    broker: Optional[Any] = None
    category: Optional[Any] = None
    hasOfferCatalog: Optional[Any] = None
    hoursAvailable: Optional[Any] = None
    isRelatedTo: Optional[Any] = None
    isSimilarTo: Optional[Any] = None
    logo: Optional[Any] = None
    offers: Optional[Any] = None
    provider: Optional[Any] = None
    providerMobility: Optional[Any] = None
    review: Optional[Any] = None
    serviceOutput: Optional[Any] = None
    serviceType: Optional[Any] = None
    slogan: Optional[Any] = None
    termsOfService: Optional[Any] = None

