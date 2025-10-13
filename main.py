from fastapi import FastAPI
from pydantic import  BaseModel

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