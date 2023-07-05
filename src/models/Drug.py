from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class Drug(Product):
    activeIngredient: Optional[Any] = None
    administrationRoute: Optional[Any] = None
    alcoholWarning: Optional[Any] = None
    availableStrength: Optional[Any] = None
    breastfeedingWarning: Optional[Any] = None
    clinicalPharmacology: Optional[Any] = None
    dosageForm: Optional[Any] = None
    doseSchedule: Optional[Any] = None
    drugClass: Optional[Any] = None
    drugUnit: Optional[Any] = None
    foodWarning: Optional[Any] = None
    includedInHealthInsurancePlan: Optional[Any] = None
    interactingDrug: Optional[Any] = None
    isAvailableGenerically: Optional[Any] = None
    isProprietary: Optional[Any] = None
    labelDetails: Optional[Any] = None
    legalStatus: Optional[Any] = None
    maximumIntake: Optional[Any] = None
    mechanismOfAction: Optional[Any] = None
    nonProprietaryName: Optional[Any] = None
    overdosage: Optional[Any] = None
    pregnancyCategory: Optional[Any] = None
    pregnancyWarning: Optional[Any] = None
    prescribingInfo: Optional[Any] = None
    prescriptionStatus: Optional[Any] = None
    proprietaryName: Optional[Any] = None
    relatedDrug: Optional[Any] = None
    rxcui: Optional[Any] = None
    warning: Optional[Any] = None

