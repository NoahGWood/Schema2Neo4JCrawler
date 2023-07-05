from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Demand(Thing):
    acceptedPaymentMethod: Optional[Any] = None
    advanceBookingRequirement: Optional[Any] = None
    areaServed: Optional[Any] = None
    asin: Optional[Any] = None
    availability: Optional[Any] = None
    availabilityEnds: Optional[Any] = None
    availabilityStarts: Optional[Any] = None
    availableAtOrFrom: Optional[Any] = None
    availableDeliveryMethod: Optional[Any] = None
    businessFunction: Optional[Any] = None
    deliveryLeadTime: Optional[Any] = None
    eligibleCustomerType: Optional[Any] = None
    eligibleDuration: Optional[Any] = None
    eligibleQuantity: Optional[Any] = None
    eligibleRegion: Optional[Any] = None
    eligibleTransactionVolume: Optional[Any] = None
    gtin: Optional[Any] = None
    gtin12: Optional[Any] = None
    gtin13: Optional[Any] = None
    gtin14: Optional[Any] = None
    gtin8: Optional[Any] = None
    includesObject: Optional[Any] = None
    ineligibleRegion: Optional[Any] = None
    inventoryLevel: Optional[Any] = None
    itemCondition: Optional[Any] = None
    itemOffered: Optional[Any] = None
    mpn: Optional[Any] = None
    priceSpecification: Optional[Any] = None
    seller: Optional[Any] = None
    serialNumber: Optional[Any] = None
    sku: Optional[Any] = None
    validFrom: Optional[Any] = None
    validThrough: Optional[Any] = None
    warranty: Optional[Any] = None

