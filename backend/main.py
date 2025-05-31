from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import model  # Our diagnosis model

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Symptoms(BaseModel):
    symptoms: list[str]
    age: int
    gender: str

@app.post("/diagnose")
async def diagnose(symptoms: Symptoms):
    """Endpoint that takes symptoms and returns possible conditions"""
    prediction = model.predict_diagnosis(
        symptoms.symptoms,
        symptoms.age,
        symptoms.gender
    )
    return {"diagnosis": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)