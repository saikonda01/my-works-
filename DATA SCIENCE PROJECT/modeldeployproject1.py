# -*- coding: utf-8 -*-
"""ModelDeployProject1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mg5tBWs93mynQ3T5rEIb-ondmVLv-uhi
"""
import streamlit

#bash pip install streamlit
import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
import pandas as pd

import streamlit as st
from sklearn.linear_model import LogisticRegression

st.title('Bankruptcy prediction')
st.sidebar.header('User input parameters')

def user_input_parameters():
  input1 = st.sidebar.selectbox('Financial flexibility',(1,.5,0))
  input2 = st.sidebar.selectbox('Credibility',(1,.5,0))
  input3 = st.sidebar.selectbox('Competitiveness',(1,.5,0))
  data = {
      'financial_flexibility': input1,
      'credibility': input2,
      'competitiveness': input3

  }

  dataframe=pd.DataFrame(data, index=[0])
  return dataframe

df=user_input_parameters()
st.subheader('User Inputs are:')
st.write(df)

#pip install openpyxl
import openpyxl
data1=pd.read_excel("D:\\DATA SCIENCE PROJECT\\bankruptcy-prevention.xlsx")
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data1['class'] = label_encoder.fit_transform(data1['class'])
categorical_columns = ['industrial_risk','management_risk','financial_flexibility','credibility','competitiveness','operating_risk']
for column in categorical_columns:
  data1[column] = label_encoder.fit_transform(data1[column])

df1=data1
columns_to_drop = ['industrial_risk', 'management_risk', 'operating_risk', 'class']
X = df1.drop(columns=columns_to_drop, axis=1)
y=df1['class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
lg=LogisticRegression(random_state=42)
lg.fit(X_train,y_train)

prediction = lg.predict(df)
prediction_proba = lg.predict_proba(df)

if prediction==1:
    a='not bankrput'
else:
    a='bankrupt'

st.subheader('Predicted Result')
st.write(f'Prediction is : {a}')