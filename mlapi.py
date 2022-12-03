from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn
import numpy as np

app = FastAPI()


# class Stats(BaseModel):
#     PTS_5: float
#     stl_5: float
#     ft_pct_5: float
#     min_5: float


#df = pd.read_csv("sample.csv")
#df.drop(["Unnamed: 4"], axis=1, inplace=True)


with open("model/ppg_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
async def root():
    return {"hello": "mlapi"}


@app.get("/predict/{pts_5}/{stl_5}/{ft_pct_5}/{min_5}")
async def predict_ppg(pts_5, stl_5, ft_pct_5, min_5):

    pred = model.predict(np.array([pts_5, stl_5, ft_pct_5, min_5]).reshape(1,-1))
    return {"prediction": pred[0]}



if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
