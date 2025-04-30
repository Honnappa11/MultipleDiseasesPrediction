# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:37:05 2024

@author: HONNAPPA M S
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetic_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Multiple Diseases Prediction/diabetic_model2.sav','rb'))

heart_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Multiple Diseases Prediction/heart_dataset2.sav','rb'))

# side bar for navigate

with st.sidebar:
    
    selected=option_menu('Multiple Diseases Prediction System',
                         ['Diabetes Prediction',
                          'Heart Diseases Prediction'
        ],default_index=0)
    
# diabetes prediction page
if selected=='Diabetes Prediction':
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the data from user
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Pregnancy count')
    with col2:   
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Genetic Diabetes Risk')
    with col2:
        Age=st.text_input('Age of the Person')
    
    # for prediction
    
    diabetic_diagnosis=''
    
    # create a button
    
    if st.button('Diabetic Test Prediction'):
        prediction=diabetic_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if prediction[0]==1:
            diabetic_diagnosis='The Person is Diabetic'
        else:
            diabetic_diagnosis='The Person is not Diabetic'
            
    st.success(diabetic_diagnosis)
    
if selected=='Heart Diseases Prediction':
    
    # page title
    st.title('Heart Diseases Prediction using Ml')
    # getting input from user
    col1,col2,col3,col4=st.columns(4)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Gender')
    with col3:
        cp=st.text_input('Chest Pain Type value')
    with col4:
        trtbps=st.text_input('Trtbps value')
    with col1:
        chol=st.text_input('Cholesterol Level value')
    with col2:
        fbs=st.text_input('FBS value')
    with col3:
         restecg=st.text_input('Restecg value')
    with col4:
        thalachh=st.text_input('Thalachh value')
    with col1:
        exng=st.text_input('Chest Pain from Exercise value')
    with col2:
        oldpeak=st.text_input('OldPeak value')
    with col3:
       slp=st.text_input('SLP value')
    with col4:
       caa=st.text_input('CAA value')
    with col1:
       thall=st.text_input('Thall value')
    
    # code for prediction
    
    diagnosis=''
    
    # create a button for prediction
    
    if st.button('Heart Test Result'): 
        prediction=heart_model.predict([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]])
        
        if prediction[0]==1:
            diagnosis='unhealthy heart'
        else:
            diagnosis='healthy heart'
        
    st.success(diagnosis)
    