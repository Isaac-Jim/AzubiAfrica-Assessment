

##  Client Subscription Prediction

### Overview

This project aims to build a predictive model that determines whether a bank client will subscribe to a term deposit based on historical marketing data. It is part of a job application assignment and demonstrates skills in data exploration, preprocessing, feature engineering, model building, and deployment.



### Dataset

The data used is from direct marketing campaigns by a  banking institution. It includes client attributes, contact information, and campaign outcomes.

We used:

* `bank-additional-full.csv` – Contains 41,188 records with 20 input features.
* Target variable: `y` (binary: `yes` or `no`).



###  Objectives

* Conduct Exploratory Data Analysis (EDA).
* Perform feature engineering and preprocessing.
* Build a machine learning model to predict `y`.
* Evaluate model performance using appropriate metrics.
* Explain insights and identify features most relevant to prediction.
* Deploy the model in a user-friendly interface 


###  Technologies & Libraries

* Python (pandas, NumPy, scikit-learn, matplotlib, seaborn)
* imbalanced-learn (for SMOTE)
  




###  Model Performance

Model used: `RandomForestClassifier` 

Metrics:

* **Accuracy**: 95.31%
* **Precision**: 93.95%
* **Recall**: 96.85%
* **F1 Score**: 95.38%
* **ROC AUC**: 95.31%

> *Note: These values will be updated based on final model output.*



###  Key Insights

Call duration strongly influences subscription rates
Subscription rates increase almost linearly with call duration from 0 to 1,000 seconds. Beyond 1,100 seconds, the trend becomes inconsistent. For effective marketing, calls should ideally last between 500 and 1,000 seconds to maximize conversion.

Clients aged 60 and above are the most likely to subscribe
Older clients, particularly those above 60, show the highest likelihood of subscribing. In contrast, clients aged 35 to 55 subscribe at significantly lower rates. Additional research is recommended to understand the barriers affecting this age group.

Occupation plays a key role in subscription behavior
Students, retirees, and unemployed individuals are the most responsive to marketing campaigns. On the other hand, entrepreneurs, service workers, and blue-collar workers have the lowest subscription rates. Marketing efforts should focus on high-performing groups, while strategies to improve uptake in low-performing segments should also be explored.

Mobile outreach is more effective than landline communication
Clients respond better to campaigns conducted through cellular calls compared to traditional telephone lines. Shifting focus toward mobile communication is likely to improve engagement.

Campaign performance across months needs clearer evaluation
The majority of marketing activities took place in May, July, and August. Although these months recorded the highest number of subscriptions, the uneven distribution of campaigns limits meaningful comparison. Running a consistent number of campaigns throughout the year will help determine which months truly yield better results.


