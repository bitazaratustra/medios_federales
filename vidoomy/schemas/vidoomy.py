from pydantic import BaseModel
from datetime import date
from typing import List

class ReportRequest(BaseModel):
    user: str
    password: str
    date_from: date
    date_to: date

class DomainRevenue(BaseModel):
    domain: str
    revenue: str

class ReportResponse(BaseModel):
    startdate: str
    enddate: str
    domains: List[DomainRevenue]
