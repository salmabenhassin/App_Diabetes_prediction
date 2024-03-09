# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:32:00 2024

@author: admin
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open("C:/Users/admin/Desktop/MachineLearning/trained_model.sav",'rb'))

#creating a function for prediction 

def diabetes_prediction(input_data):
 
    #changing the input_data to numpy array
    input_array=np.asarray(input_data)
    print(input_array)

    # reshape the array as we are predecting for one instance 
    input_resshaped = input_array.reshape(1,-1)
    print(input_resshaped)

    y_prediction = loaded_model.predict(input_resshaped)
    print(y_prediction)

    if (y_prediction[0]==0):
        return 'the person is not diabetic'
    else:
        return 'the person is  diabetic'
        



def main():
    #giving a title
    st.title('Diabetes Prediction web App')
    st.markdown(
        """
        <style>
        .title {
            color: blue;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
            font-weight: thin; /* Use thin font weight for a thinner font */
        }
        .stApp {
            background-color: rgba(128, 0, 128, 0.2); /* Violet transparent background */
        }
        .button {
            background-color: blue; /* Blue button */
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-top: 20px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #005353;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
 #   Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
    
    Pregnancies = st.text_input('number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure level')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value') 
    Age = st.text_input('Age of the Person')
    
    #code for Prediction
    diagnosis = ''
     
    #creating a  button for prediction
    if st.button('Diabete Test Result :'):
        diagnosis=diabetes_prediction([Pregnancies ,Glucose , BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
    