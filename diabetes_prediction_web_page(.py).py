# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 09:33:09 2024

@author: LOKESH
"""


import numpy as np
import streamlit as st
import pickle 
from streamlit_option_menu import option_menu

with st.sidebar:
    selected= option_menu('multiple disease prediction',['diabetes','parkinson'],default_index = 0)
    
if (selected=='diabetes'):



 loaded_model = pickle.load(open('C:/Users/LOKESH/Downloads/diabetes_model.sav','rb'))

 def diabetes_prediction(input_data):
    input_data_as_nparray = np.asarray(input_data)
    input_data_reshaped = input_data_as_nparray.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    
    if (prediction[0]==0):
        return 'the person is not diabetic'
    else :
        return 'the person is diabetic'
        
    
    
 def main():
    st.title('Diabetes Prediction')
    
    
    pregnancies=st.text_input("Number of Pregnancies")
    glucose=st.text_input("glucose level")
    blood_pressure = st.text_input("Blood Pressure value")
    skinthickness = st.text_input("skin thickness")
    insulin = st.text_input('insulin value')
    BMI=st.text_input('BMI')
    diabetespedigreefunction = st.text_input('Diabetes Pedigree Function value')
    age = st.text_input('enter age')
    
    diagnosis=''
    
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([pregnancies,glucose,blood_pressure,skinthickness,insulin,BMI,diabetespedigreefunction,age])
 
                                      
    st.success(diagnosis)
     
else :
 if(selected == 'parkinson'):
   def main():
       st.title('parkinson prediction')
       
if __name__ =='__main__':
 main()                                 
                                     
                                       
                                       