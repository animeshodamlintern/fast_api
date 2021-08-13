from fastapi import FastAPI, responses
import json
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.params import File
import uuid
import aiofiles
from requests import Response

app = FastAPI()

@app.get('/')
def index():
    return {
        'message': 'Hello, We are from Optimum Data Analytics'
    }

@app.post('/bindu/{path}')
async def bindu(path):
    res = json.dumps({
        'text': "transfer success"
    })
    return Response(res)


@app.post('/v1/uploads')
async def create_img_file(image: UploadFile = File(...)):
    if not image.content_type.startswith('image'):
        raise HTTPException(status_code=400)

    temp_filename = uuid.uuid4().__str__()
    ext = image.filename.split('.')[-1]
    filename = "{}.{}".format(temp_filename, ext)

    async with aiofiles.open(filename, 'wb') as fp:
        content = await image.read()
        await fp.write(content)

    URL = '/bindu/{}'.format(filename)
    return responses.RedirectResponse(url=URL)