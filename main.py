import csv
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from medios_federales.cruds import contactos as crud_contactos
from database import SessionLocal, engine

from medios_federales.models import contactos as model_contactos
from medios_federales.schemas.contactos import ContactosContactos
model_contactos.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para cargar datos desde CSV
@app.post("/load-csv/")
def load_csv(db: Session = Depends(get_db)):
    try:
        with open('contactos.csv', mode='r', newline='', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                item = {
                    "pais": row["Pais"],
                    "localidad": row["Localidad"],
                    "company": row["Company o Grupo de medios"],
                    "company_domain": row["Company Domain"],
                    "CMS": row["CMS"],
                    "SW": row["SW"],
                    "email": row["Email"],
                    "tel": row["Tel"],
                    "full_name": row["FullName"],
                    "first_name": row["FirstName"]
                }

                db.begin()
                try:
                    crud_contactos.create_item(db=db, item=item)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    raise HTTPException(status_code=500, detail=f"Error loading CSV data: {str(e)}")

        return {"message": "CSV data loaded successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading CSV data: {str(e)}")
    finally:
        file.close()



@app.get("/contactos/nombre-apellido",
         response_model=List[ContactosContactos])

def get_nombre_apellido():
    db = SessionLocal()
    return crud_contactos.datos_contactos(db)
