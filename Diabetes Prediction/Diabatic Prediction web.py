# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:20:53 2023

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as st

#loaded_model=pickle.load(open('E:/Diabatic prediction/trained_model.sav','rb'))
loaded_model=pickle.load(open('F:/Diabatic prediction final/trained_model.sav','rb'))

#creating a function for prediction

def diabetics_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
   # std_data = scaler.transform(input_data_reshaped)
   # print(std_data)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
def main():
      
      #giving  a title
      st.title('Check your Diabatic state')
      
      #getting the input fromthe user
      
      Pregnancies= st.text_input('Number of Preagnencies')
      Glucose= st.text_input('Glucose level')
      BloodPressure= st.text_input('Blood Pressure Level')
      SkinThickness= st.text_input('Skin thickness Value')
      Insulin= st.text_input('Insulin level')
      BMI= st.text_input('BMI value')
      DiabetesPedigreeFunction= st.text_input('Diabatic Pedigree Function value')
      Age= st.text_input('Age of the person')
      
      
      #code for prediction
      diagnosis=''
      
      #creating a button for prediction
      
      if st.button('Diabetes test result'):
          
          diagnosis=diabetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
          
      st.success(diagnosis)
          
          
          
          
          

if __name__=='__main__':
     main()

          
  

     
    
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
   