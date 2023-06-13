from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from genranper import generaterandom
app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


valid_api_key = "abid2004"

# API key validation dependency
def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != valid_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

@app.get("/generate/{n}")
def generate_random_data(n: int, api_key: str = Depends(validate_api_key)):
    results = generaterandom(n)
    data = [{"person_name": person_name, "fake_email": fake_email} for person_name, fake_email in results]
    return {"data": data}
