from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

class Item(BaseModel):
    PTS_5: float
    stl_5:float
    ft_pct_5: float
    min_5: float
    
with open("model/ppg_model.pkl", "rb") as f:
    model = pickle.load(f)



@app.get("/")
async def scoring_endpoint(item:Item):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    y_het = model.predict(df)
    return {"prediction": int(y_hat)}
    
@app.get("/predict/{filename}")
async def predict_endpoint(filename):
    df = pd.DataFrame([filename.dict().values()], columns=filename.dict().keys())
    return {"original data": df}
    #y_het = model.predict(df)
    #return {"prediction": int(y_hat)}
    
    
@app.get("/test")
async def test_hello():
    return {"message": "hello"}
"""
@app.get("/test/")
async def test(file):
    df = pd.read_csv("sample.csv",index_col=False)
    return df
"""