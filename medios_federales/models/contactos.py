from sqlalchemy import Column, Integer, String
from database import Base

class Contactos(Base):
    __tablename__ = "contactos"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), index=True)
    first_name = Column(String(255), index=True)
    pais = Column(String(255), index=True)
    localidad = Column(String(255), index=True)
    company = Column(String(255), index=True)
    company_domain = Column(String(255), index=True)
    domain = Column(String(255), index=True)
    CMS = Column(String(255), index=True)
    SW = Column(String(255), index=True)
    email = Column(String(255), index=True)
    tel = Column(String(255), index=True)
