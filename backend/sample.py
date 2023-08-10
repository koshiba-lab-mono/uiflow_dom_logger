from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PostData(BaseModel):
    content: str


@app.get("/")
async def get_data(arg: int = 10):
    content = {"sampleKey": arg * 10}
    return content


@app.post("/post/")
async def post_data(content: PostData):
    print(content)
    return {"response": "ok"}
