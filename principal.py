from typing import Tuple
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from PIL import Image
import io
import cv2
import numpy as np
import uvicorn

app = FastAPI()

def calcular_area_ferida(image: Image.Image) -> Tuple[Image.Image, float, float]:
    image_np = np.array(image)
    image_gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    _, limiar = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(limiar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maior_contorno = max(contornos, key=cv2.contourArea, default=None)
    if maior_contorno is not None:
        area_pixels = cv2.contourArea(maior_contorno)
        cv2.drawContours(image_np, [maior_contorno], -1, (0, 255, 0), 2)
    else:
        area_pixels = 0

    area_cm2 = (area_pixels * (0.0667 ** 2)) / 100  # Converting to cm²
    image_with_contour = Image.fromarray(image_np)
    return image_with_contour, area_pixels, area_cm2

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")

    try:
        image = Image.open(file.file).convert("RGB")
        image_with_contour, area_pixels, area_cm2 = calcular_area_ferida(image)
        img_io = io.BytesIO()
        image_with_contour.save(img_io, 'JPEG')
        img_io.seek(0)
        headers = {
            "Content-Disposition": f"attachment; filename=processed_{file.filename}",
            "Area-Pixels": str(area_pixels),
            "Area-Cm2": str(area_cm2)
        }
        return StreamingResponse(content=img_io, media_type="image/jpeg", headers=headers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", encoding='utf-8') as f:
        return HTMLResponse(content=f.read(), status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
