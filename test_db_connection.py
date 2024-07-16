from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# Configura la URL de conexión a la base de datos
DATABASE_URL = "mysql+pymysql://medios_federales:m3d10s@localhost/medios_federales"

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Intenta crear una sesión para verificar la conexión
try:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    result = session.execute(text("SELECT 1"))  # Ejecuta una consulta simple para verificar la conexión
    print("Conexión exitosa a la base de datos MySQL")
except OperationalError as e:
    print(f"Error al conectar a la base de datos MySQL: {str(e)}")
finally:
    session.close()  # Cierra la sesión después de usarla
