from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
import joblib
import uvicorn

app = FastAPI(title="API Startup", description="with FastAPI by Antonio Magliari", version="1.0")

## Basemodel
class CompanyData(BaseModel):
    rd: float =162597
    adm: float =151377
    mrk: float =443898

## blocco per la cache del mio modello
@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model 
    model = joblib.load("startup.pkl")
    print(" MODEL LOADED!!")
    return model


@app.get("/")
def home():
    return {" ---->          http://localhost:8000/    <----------"}

@app.get("/predict")
async def predictget(data:CompanyData=Depends()):
    try:
        X = [[data.rd, data.adm, data.mrk]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")

## secca POST per streamlit o chiamate esterne
@app.post("/predict")
async def predictpost(data:CompanyData):
    try:
        X = [[data.rd, data.adm, data.mrk]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")

###############################################################################################

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
