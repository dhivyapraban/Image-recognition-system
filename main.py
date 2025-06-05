from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import shutil
import cv2
import os

app = FastAPI()
model = YOLO("yolov8n.pt")

UPLOAD_DIR = r"path"
RESULTS_DIR = r"path"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=r"path"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open(r"path", "r") as f:
        return f.read()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filename = file.filename.replace(" ", "_")

    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(file_path)
    annotated_frame = results[0].plot()

    output_filename = f"annotated_{filename}"
    output_path = os.path.join(RESULTS_DIR, output_filename)
    cv2.imwrite(output_path, annotated_frame)

    result_image = f"static/results/{output_filename}"
    return {"result_image": result_image}
