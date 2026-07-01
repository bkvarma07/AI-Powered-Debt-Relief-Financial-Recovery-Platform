from fastapi import FastAPI

app = FastAPI(
    title="FinRelief AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "FinRelief AI Backend Running Successfully"
    }