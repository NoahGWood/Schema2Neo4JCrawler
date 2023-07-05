from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class JobPosting(Thing):
    applicantLocationRequirements: Optional[Any] = None
    applicationContact: Optional[Any] = None
    baseSalary: Optional[Any] = None
    datePosted: Optional[Any] = None
    directApply: Optional[Any] = None
    educationRequirements: Optional[Any] = None
    eligibilityToWorkRequirement: Optional[Any] = None
    employerOverview: Optional[Any] = None
    employmentType: Optional[Any] = None
    employmentUnit: Optional[Any] = None
    estimatedSalary: Optional[Any] = None
    experienceInPlaceOfEducation: Optional[Any] = None
    experienceRequirements: Optional[Any] = None
    hiringOrganization: Optional[Any] = None
    incentiveCompensation: Optional[Any] = None
    industry: Optional[Any] = None
    jobBenefits: Optional[Any] = None
    jobImmediateStart: Optional[Any] = None
    jobLocation: Optional[Any] = None
    jobLocationType: Optional[Any] = None
    jobStartDate: Optional[Any] = None
    occupationalCategory: Optional[Any] = None
    physicalRequirement: Optional[Any] = None
    qualifications: Optional[Any] = None
    relevantOccupation: Optional[Any] = None
    responsibilities: Optional[Any] = None
    salaryCurrency: Optional[Any] = None
    securityClearanceRequirement: Optional[Any] = None
    sensoryRequirement: Optional[Any] = None
    skills: Optional[Any] = None
    specialCommitments: Optional[Any] = None
    title: Optional[Any] = None
    totalJobOpenings: Optional[Any] = None
    validThrough: Optional[Any] = None
    workHours: Optional[Any] = None

