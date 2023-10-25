# Import necessary libraries and modules
from fastapi import FastAPI
import uvicorn
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from E_learning_recommender_system.pipeline.prediction import PredictionPipeline

# Define a user input for the recommender system (initial value)
user_input = "Recommender System"

# Create a FastAPI app instance
app = FastAPI(docs_url="/docs", redoc_url="/redoc")

# Define a route to redirect to the API documentation
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Define a route for training the recommender system
@app.get("/train")
async def training():
    try:
        # Run the "main.py" script for training
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Define a route for making predictions using the recommender system
@app.post("/predict")
async def predict_route(text):
    try:
        # Create an instance of the PredictionPipeline
        obj = PredictionPipeline()
        # Use the pipeline to make a prediction based on the input text
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

# Run the FastAPI app using UVicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
