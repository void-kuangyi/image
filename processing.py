from PIL import Image, ImageOps
import requests
from io import BytesIO

def function(variable):
    # url = f'https://maps.googleapis.com/maps/api/staticmap?center={variable}&zoom=16&size=400x400&maptype=satellite&key=AIzaSyDLLb5FAlXngV3Q16xGZAkNKxwMCNMJBtc'
    url = f'https://maps.googleapis.com/maps/api/staticmap?center=51.450102,%205.489436&zoom=16&size=400x400&maptype=satellite&key=AIzaSyDLLb5FAlXngV3Q16xGZAkNKxwMCNMJBtc'
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("L")

    # Resize smoothly down to 16x16 pixels
    imgSmall = img.resize((4,4),resample=Image.BILINEAR)
    imgGrey = ImageOps.grayscale(imgSmall)
    rawData = imgGrey.load()
    data = []
    for y in range(4):
        for x in range(4):
            data.append(rawData[x,y])
    return str(data).replace("[","").replace("]","")