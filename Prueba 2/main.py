from fastapi import FastAPI
from routes.jumbo_products import router as jumbo_products

app = FastAPI()

app.include_router(jumbo_products)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CSV Generator API"}