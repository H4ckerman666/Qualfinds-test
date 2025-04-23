from traceback import print_exc
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import requests
from utils.scrapper import get_jumbo_products

router = APIRouter()


class URLRequest(BaseModel):
    url: str


@router.post("/get_jumbo_products/")
async def scrap_jumbo_products(request: URLRequest) -> Dict[str, Any]:
    url = request.url

    try:
        response = requests.get(url)
        response.raise_for_status()

        products = get_jumbo_products(url)
        return {"url": url, "products": products}

    except requests.ConnectionError:
        raise HTTPException(status_code=503, detail="Error de conexión al servidor.")

    except requests.Timeout:
        raise HTTPException(
            status_code=504, detail="La solicitud al servidor ha expirado."
        )

    except requests.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))

    except Exception as err:
        print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno: {err}")
