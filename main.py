from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    timestamp = datetime.now().isoformat()
    return {
        "message": "Hello World",
        "timestamp": timestamp
    }