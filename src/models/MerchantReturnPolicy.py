from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class MerchantReturnPolicy(Thing):
    additionalProperty: Optional[Any] = None
    applicableCountry: Optional[Any] = None
    customerRemorseReturnFees: Optional[Any] = None
    customerRemorseReturnLabelSource: Optional[Any] = None
    customerRemorseReturnShippingFeesAmount: Optional[Any] = None
    inStoreReturnsOffered: Optional[Any] = None
    itemCondition: Optional[Any] = None
    itemDefectReturnFees: Optional[Any] = None
    itemDefectReturnLabelSource: Optional[Any] = None
    itemDefectReturnShippingFeesAmount: Optional[Any] = None
    merchantReturnDays: Optional[Any] = None
    merchantReturnLink: Optional[Any] = None
    refundType: Optional[Any] = None
    restockingFee: Optional[Any] = None
    returnFees: Optional[Any] = None
    returnLabelSource: Optional[Any] = None
    returnMethod: Optional[Any] = None
    returnPolicyCategory: Optional[Any] = None
    returnPolicyCountry: Optional[Any] = None
    returnPolicySeasonalOverride: Optional[Any] = None
    returnShippingFeesAmount: Optional[Any] = None

