from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class FundingAgency(Thing):
    actionableFeedbackPolicy: Optional[Any] = None
    address: Optional[Any] = None
    aggregateRating: Optional[Any] = None
    alumni: Optional[Any] = None
    areaServed: Optional[Any] = None
    award: Optional[Any] = None
    brand: Optional[Any] = None
    contactPoint: Optional[Any] = None
    correctionsPolicy: Optional[Any] = None
    department: Optional[Any] = None
    dissolutionDate: Optional[Any] = None
    diversityPolicy: Optional[Any] = None
    diversityStaffingReport: Optional[Any] = None
    duns: Optional[Any] = None
    email: Optional[Any] = None
    employee: Optional[Any] = None
    ethicsPolicy: Optional[Any] = None
    event: Optional[Any] = None
    faxNumber: Optional[Any] = None
    founder: Optional[Any] = None
    foundingDate: Optional[Any] = None
    foundingLocation: Optional[Any] = None
    funder: Optional[Any] = None
    funding: Optional[Any] = None
    globalLocationNumber: Optional[Any] = None
    hasCredential: Optional[Any] = None
    hasMerchantReturnPolicy: Optional[Any] = None
    hasOfferCatalog: Optional[Any] = None
    hasPOS: Optional[Any] = None
    interactionStatistic: Optional[Any] = None
    isicV4: Optional[Any] = None
    iso6523Code: Optional[Any] = None
    keywords: Optional[Any] = None
    knowsAbout: Optional[Any] = None
    knowsLanguage: Optional[Any] = None
    legalName: Optional[Any] = None
    leiCode: Optional[Any] = None
    location: Optional[Any] = None
    logo: Optional[Any] = None
    makesOffer: Optional[Any] = None
    member: Optional[Any] = None
    memberOf: Optional[Any] = None
    naics: Optional[Any] = None
    nonprofitStatus: Optional[Any] = None
    numberOfEmployees: Optional[Any] = None
    ownershipFundingInfo: Optional[Any] = None
    owns: Optional[Any] = None
    parentOrganization: Optional[Any] = None
    publishingPrinciples: Optional[Any] = None
    review: Optional[Any] = None
    seeks: Optional[Any] = None
    slogan: Optional[Any] = None
    sponsor: Optional[Any] = None
    subOrganization: Optional[Any] = None
    taxID: Optional[Any] = None
    telephone: Optional[Any] = None
    unnamedSourcesPolicy: Optional[Any] = None
    vatID: Optional[Any] = None

