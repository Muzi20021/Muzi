from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image
import requests
from io import BytesIO

app = FastAPI()
yolo_model = YOLO('yolov9c.pt')

def detect_persons_in_image(image: Image):
    return yolo_model.predict(source=image, classes=[0], conf=0.4)[0] if image else None

def save_image_to_disk(image: Image, path: str):
    image.save(path)

def process_bytes_to_image(data: bytes) -> Image:
    return Image.open(BytesIO(data))

async def process_image_for_detection(image: Image):
    result_image = detect_persons_in_image(image)
    if result_image:
        save_path = "wynik.jpg"
        save_image_to_disk(result_image, save_path)
        return {"Liczba wykrytych osób na obrazie: ": len(result_image.boxes), "Wynik został zapisany: ": save_path}
    raise HTTPException(status_code=500, detail="Nie wykryto żadnych osób.")

async def get_image_from_url(url: str) -> Image:
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

@app.get("/detect_local_image")
async def detect_persons_in_local_image(file_path: str):
    try:
        image = Image.open(file_path)
        return await process_image_for_detection(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/detect_online_image")
async def detect_persons_in_online_image(url: str):
    try:
        image = await get_image_from_url(url)
        return await process_image_for_detection(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect_uploaded_image")
async def detect_persons_in_uploaded_image_endpoint(file: UploadFile = File(...)):
    try:
        image = process_bytes_to_image(await file.read())
        return await process_image_for_detection(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
