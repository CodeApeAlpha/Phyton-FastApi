# pip install python-multipart

from fastapi import FastAPI, Form
import uvicorn
app = FastAPI()


@app.post("/lanform/")
async def language(Name: str = Form(...), Type: str = Form(...)):
    return {
        "Name": Name, "type": Type
    }


@app.post("/lanjson/")
async def language(Name: str, Type: str):
    return {
        "Name": Name, "type": Type
    }

uvicorn.run(app)
