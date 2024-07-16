from pydantic import BaseModel, validator
from datetime import date, datetime

class ContactosBase(BaseModel):
    id: str
    
class ContactosContactos(ContactosBase):     
    full_name: str
    first_name: str
    email: str
    tel: str

class ContactosUbicacion(ContactosBase):
    pais: str
    localidad: str
    
class Company(ContactosBase):
    company: str
    company_domain: str
    domain: str
    CMS: str
    SW: str
    
class All(ContactosBase):
    contacto: ContactosContactos
    ubicacion: ContactosUbicacion
    company: Company