import csv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from medios_federales.cruds import contactos as crud_contactos
from medios_federales.database import SessionLocal, engine

from medios_federales.models import contactos as model_contactos
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
                # Iniciar una transacción explícitamente
                db.begin()
                try:
                    # Llama a la función para crear un ítem en la base de datos
                    crud_contactos.create_item(db=db, item=item)
                    # Confirmar la transacción
                    db.commit()
                except Exception as e:
                    # Revertir la transacción en caso de error
                    db.rollback()
                    raise HTTPException(status_code=500, detail=f"Error loading CSV data: {str(e)}")
        
        return {"message": "CSV data loaded successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading CSV data: {str(e)}")
    finally:
        # Cerrar el archivo CSV explícitamente
        file.close()
