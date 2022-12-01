from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    PTS_5: float
    stl_5:float
    ft_pct_5: float
    min_5: float


@app.get("/")
async def scoring_endpoint(item:Item):
    return item