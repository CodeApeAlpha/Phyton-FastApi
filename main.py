from fastapi import FastAPI

# Pydantic- is a library with data type validation
# https://fastapi.tiangolo.com/tutorial/body/?h=basemodel#import-pydantics-basemodel
from pydantic import BaseModel

# Typing
from typing import Optional

# Uvicorn
import uvicorn


class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None


class PackageOut(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


app = FastAPI()


@app.get('/')
async def index():
    return {
        "hello": "Word"
    }


# Pydantic
@app.post("/BaseModel/")
async def baseModel(item: PackageIn):
    print(item.name.capitalize())
    return {
        **item.dict()
    }


@app.post("/package/", response_model=PackageOut,
          response_model_exclude_unset=False)
# response_model_include={"description"})  # response_model_exclude -> to exclude certain fields
async def make_package(package: PackageIn):
    return package


# @app.post("/package/{priority}")
# async def make_package(priority: int, package: Package, value: int):
#     print(package.dict())
#     return {
#         "priority": priority, **package.dict(), "value": value
#     }

# @app.post("/package/{priority}")
# async def make_package(priority: int, package: Package, value: int):
#     return {
#         "priority": priority,
#         "package": {
#                "name": package.name,
#                "number": package.number,
#                 "description":package.description
#         },
#                    # ** package.dict(),
#         "value": value
#     }


# # path parameter
# @app.get("/look/{look_Id}")
# async def look(look_Id: int):
#     return {
#         "look_id": look_Id
#     }
#
#
# # query parameter
# @app.get("/look")
# async def look(number: int, text: str):
#     return {
#         "num": number,
#         "text": text
#     }


uvicorn.run(app)
