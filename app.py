from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import Test

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()


class Item(BaseModel):
    name : str
    number : int

@app.get("/")
async def first_get():
    example = session.query(Test).filter(Test.GENDER == "남자").all()
    print(example)
    for item in example:
        print(item.__dict__)

    serialized_example = [item.to_dict() for item in example]
    return serialized_example

