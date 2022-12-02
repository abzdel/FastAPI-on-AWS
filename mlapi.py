from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn

app = FastAPI()

class Stats(BaseModel):
    PTS_5: float
    stl_5:float
    ft_pct_5: float
    min_5: float
    
    

df = pd.read_csv("sample.csv")
df.drop(["Unnamed: 4"], axis=1, inplace=True)

    
with open("model/ppg_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
async def root():
    return {"hello": "mlapi"}


  
@app.get("/predict")
async def predict_ppg(data:Stats):
    
    data = data.dict()
    PTS_5 = data["PTS_5"]
    stl_5 = data["stl_5"]
    ft_pct_5 = data["ft_pct_5"]
    min_5 = data["min_5"]
    
    pred = model.predict([[PTS_5, stl_5, ft_pct_5, min_5]])
    return {"prediction": pred}


    
    
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')