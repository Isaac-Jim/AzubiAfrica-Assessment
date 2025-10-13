from fastapi import FastAPI
from pydantic import  BaseModel
import joblib

app =  FastAPI()

class   subscription_features(BaseModel):
    age : int
    job  : str
    education  :  str
    duration   :  float
    campaign  :    str
    pdays     :     float
    previous  :     bool
    emp_var_rate    :   float     
    cons_price_idx   :  float
    cons_conf_idx     : float
    euribor3m          :float
    nr_employed         : bool
    marital_married      :   bool
    marital_single        :  bool
    marital_unknown        : bool  
    default_unknown         :bool
    default_yes             :bool
    housing_unknown         :bool
    housing_yes             :bool
    loan_unknown            :bool
    loan_yes                :bool
    poutcome_nonexistent    :bool
    poutcome_success        :bool
    day_of_week_mon         :bool
    day_of_week_thu         :bool
    day_of_week_tue         :bool
    day_of_week_wed         :bool
    contact_telephone       :bool

# creating an end point for prediction

@app.post("predict_subscription")
def  predict (data :subscription_features):
    features =[[

    data.age,
    data.job , 
    data.education ,  
    data.duration , 
    data.campaign ,     
    data.pdays ,         
    data.previous ,   
    data.emp_var_rate,        
    data.cons_price_idx,     
    data.cons_conf_idx,      
    data.euribor3m   ,       
    data.nr_employed  ,       
    data.marital_married,      
    data.marital_single ,        
    data.marital_unknown ,       
    data.default_unknown  ,       
    data.default_yes       ,      
    data.housing_unknown    ,     
    data.housing_yes         ,    
    data.loan_unknown         ,   
    data.loan_yes              , 
    data.poutcome_nonexistent   , 
    data.poutcome_success        ,
    data.day_of_week_mon         ,
    data.day_of_week_thu         ,
    data.day_of_week_tue         ,
    data.day_of_week_wed        ,
    data.contact_telephone 

    ]]

    #load model

    model = joblib.load("Random_Forest_1.0")

    results = model.predict(features)[0]

    return {f"subscription package indicates ":{results}}