from PIL import Image, ImageOps
import requests
from io import BytesIO

def function():
    url = "https://maps.googleapis.com/maps/api/staticmap?center=51.450102,%205.489436&zoom=16&size=400x400&key=AIzaSyDLLb5FAlXngV3Q16xGZAkNKxwMCNMJBtc"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('L')  

    # Resize smoothly down to 16x16 pixels
    imgSmall = img.resize((5,5),resample=Image.BILINEAR)
    # imgGrey = ImageOps.grayscale(imgSmall)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    rawData = result.load()
    data = []
    for y in range(5):
        for x in range(5):
            data.append(rawData[x,y])
    return str(data[0])