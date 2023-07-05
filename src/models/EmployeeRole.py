from pydantic import BaseModel
from models.OrganizationRole import OrganizationRole

from typing import Optional, Any

class EmployeeRole(OrganizationRole):
    baseSalary: Optional[Any] = None
    salaryCurrency: Optional[Any] = None

