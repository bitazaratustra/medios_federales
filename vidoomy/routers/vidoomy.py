from fastapi import APIRouter, HTTPException
import requests
import xml.etree.ElementTree as ET
from vidoomy.schemas.vidoomy import ReportRequest, ReportResponse, DomainRevenue

router = APIRouter()

@router.post("/api/domain", response_model=ReportResponse)
def get_domain_report(request: ReportRequest):
    url = "https://login.vidoomy.com/api/domain"
    payload = {
        "user": request.user,
        "password": request.password,
        "date_from": request.date_from.strftime('%Y/%m/%d'),
        "date_to": request.date_to.strftime('%Y/%m/%d')
    }

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Vidoomy API")

    root = ET.fromstring(response.content)
    startdate = root.find('startdate').text
    enddate = root.find('enddate').text
    domains = []

    for entry in root.findall('.//entry'):
        domain = entry.find('domain').text
        revenue = entry.find('revenue').text
        domains.append(DomainRevenue(domain=domain, revenue=revenue))

    return ReportResponse(startdate=startdate, enddate=enddate, domains=domains)
