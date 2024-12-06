from fastapi import FastAPI
<<<<<<< HEAD
from app.api.v1.endpoints import router as api_router
from app.db.base import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")
=======
import joblib  
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the model using joblib
model = joblib.load("model/model.joblib")  

# Define a request body schema
class InputData(BaseModel):
    data: list

# Define a route for the root
@app.get("/hello")
def read_hello():
    return {"message": "Hello World! the ,thanks you "}

# Define a route for making predictions
@app.post("/predict")
def predict(input_data: InputData):
    print(f"Received data: {input_data.data}")
    try:
        data = input_data.data
        predictions = model.predict([data])
        return {"predictions": predictions.tolist()}
    except Exception as e:
        return {"error": str(e)}
>>>>>>> 965fb520131e29bb81daf4ecdef43a9464111929
