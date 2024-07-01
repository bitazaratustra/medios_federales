from pydantic import BaseModel, validator
from datetime import date, datetime

class ReportRequest(BaseModel):
    user: str
    password: str
    date_from: str
    date_to: str

    @validator('date_from', 'date_to', pre=True)
    def parse_date(cls, value):
        try:
            return datetime.strptime(value, '%Y/%m/%d').date()
        except ValueError:
            raise ValueError('Date format must be YYYY/MM/DD')

class DomainRevenue(BaseModel):
    domain: str
    revenue: str

class ReportResponse(BaseModel):
    startdate: str
    enddate: str
    domains: list[DomainRevenue]
