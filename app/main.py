from fastapi import FastAPI

app = FastAPI(title="ShipIt API")


@app.get("/")
def home():
    return {"message": "ShipIt API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
