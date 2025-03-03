from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from TextSummarizer.pipeline.prediction import PredictionPipeline
import uvicorn
import sys
import os

text: str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url = "/docs")

@app.get("/train")
async def training():
    try:
        os.system("python3.12 main.py")
        return Response("Training Successful !")
    
    except Exception as e:
        return Response(f"Error Occured! {e}")
    
@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8080)