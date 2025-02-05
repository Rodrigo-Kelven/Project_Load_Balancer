from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "API 4"}
