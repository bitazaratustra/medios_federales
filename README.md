# Medios Federales API

Esta API, construida con FastAPI, permite comunicarse con la API de Vidoomy para obtener métricas sobre publicidad programática.

## Requisitos

- Python 3.10+
- FastAPI
- requests
- uvicorn

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/REPO_NAME.git
    cd REPO_NAME
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicia el servidor de desarrollo:

    ```bash
    uvicorn main:app --reload
    ```

2. La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### `POST /api/domain`

Obtiene el reporte de ingresos por dominio para el rango de fechas especificado.

**Parámetros de solicitud:**

```json
{
    "IsOpenAuction" : "true",
    "HasPrivateAuction" : "true", 
    "HasDirectDeal" : "true",
    "IsHeaderBidding": "true",
    "IsAuctionPackages" : "true"

}
