from fastapi import FastAPI  
from pydantic import BaseModel ,Field
from typing import Annotated 
import pickle
from fastapi.responses import JSONResponse

app = FastAPI()

#import the ml model
import joblib

model = joblib.load('Model_decision.pkl')

class inputdata(BaseModel):

    age: Annotated[int,Field(...,description='Enter the age',gt=0,lt=150)]
    sex :Annotated[int,Field(...,description='Enter the sex',example=['Must be in 1 or zero'])]
    cp : Annotated[int,Field(...,description='Enter the cp ')]
    trestbps: Annotated[int,Field(...,description='enter the trestbps')]
    chol: Annotated[int,Field(...,description='Enter the chol')]
    fbd: Annotated[int,Field(...,description='Enter the fbs')]
    restecg: Annotated[int,Field(...,description='Enter the rectage')]
    thalach:Annotated[int,Field(...,description='Enter the thalach')]
    exang : Annotated[int,Field(...,description='Enter the exang')]
    oldpeak:Annotated[float,Field(...,description= 'enter the oldpeak')]
    slope:Annotated[int,Field(...,description='Enter the slope')]
    ca:Annotated[int,Field(...,description='Enter the ca')]
    thal:Annotated[int,Field(...,description='Enter the thal')]




@app.get('/')
def hellow_world():
    return {'message':'Welcome to the heart diseases predictor'}



@app.post('/predictor')
def model_predictor(data : inputdata):
    print(data.age)
    print(data.sex)
    print(data.cp)
    print(data.trestbps)
    print(data.chol)
    print(data.fbd)
    print(data.restecg)
    print(data.thalach)
    print(data.exang)
    print(data.oldpeak)
    print(data.slope)
    print(data.ca)
    print(data.thal)

@app.post('/predictor_ml')
def model_predictor(data: inputdata):
    input_data = [[
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbd,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]]

    prediction = model.predict(input_data)[0]

    return JSONResponse(status_code=200, content={'predicted_category': int(prediction)})
