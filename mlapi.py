from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn

app = FastAPI()

class Item(BaseModel):
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
async def scoring_endpoint(item:Item):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    y_hat = model.predict(df)
    return {"prediction": y_hat}


    
@app.get("/items")
async def create_item(item: Item):
    return item
    
    
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')