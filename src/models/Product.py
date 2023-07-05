from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Product(Thing):
    additionalProperty: Optional[Any] = None
    aggregateRating: Optional[Any] = None
    asin: Optional[Any] = None
    audience: Optional[Any] = None
    award: Optional[Any] = None
    brand: Optional[Any] = None
    category: Optional[Any] = None
    color: Optional[Any] = None
    countryOfAssembly: Optional[Any] = None
    countryOfLastProcessing: Optional[Any] = None
    countryOfOrigin: Optional[Any] = None
    depth: Optional[Any] = None
    funding: Optional[Any] = None
    gtin: Optional[Any] = None
    gtin12: Optional[Any] = None
    gtin13: Optional[Any] = None
    gtin14: Optional[Any] = None
    gtin8: Optional[Any] = None
    hasAdultConsideration: Optional[Any] = None
    hasEnergyConsumptionDetails: Optional[Any] = None
    hasMeasurement: Optional[Any] = None
    hasMerchantReturnPolicy: Optional[Any] = None
    height: Optional[Any] = None
    inProductGroupWithID: Optional[Any] = None
    isAccessoryOrSparePartFor: Optional[Any] = None
    isConsumableFor: Optional[Any] = None
    isFamilyFriendly: Optional[Any] = None
    isRelatedTo: Optional[Any] = None
    isSimilarTo: Optional[Any] = None
    isVariantOf: Optional[Any] = None
    itemCondition: Optional[Any] = None
    keywords: Optional[Any] = None
    logo: Optional[Any] = None
    manufacturer: Optional[Any] = None
    material: Optional[Any] = None
    mobileUrl: Optional[Any] = None
    model: Optional[Any] = None
    mpn: Optional[Any] = None
    negativeNotes: Optional[Any] = None
    nsn: Optional[Any] = None
    offers: Optional[Any] = None
    pattern: Optional[Any] = None
    positiveNotes: Optional[Any] = None
    productID: Optional[Any] = None
    productionDate: Optional[Any] = None
    purchaseDate: Optional[Any] = None
    releaseDate: Optional[Any] = None
    review: Optional[Any] = None
    size: Optional[Any] = None
    sku: Optional[Any] = None
    slogan: Optional[Any] = None
    weight: Optional[Any] = None
    width: Optional[Any] = None

