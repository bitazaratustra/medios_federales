from sqlalchemy import Column, Integer, String
from database import Base

class Contactos(Base):
    __tablename__ = "contactos"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    first_name = Column(String, index=True)
    pais = Column(String, index=True)
    localidad = Column(String, index=True)
    company = Column(String, index=True)
    company_domain = Column(String, index=True)
    domain = Column(String, index=True)
    CMS = Column(String, index=True)
    SW = Column(String, index=True)
    email = Column(String, index=True)
    tel = Column(String, index=True)
