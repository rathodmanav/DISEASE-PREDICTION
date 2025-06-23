# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 10:35:23 2025

@author: Manav
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav', "rb"))
heart_disease_model = pickle.load(open('heart_disease_model.sav', "rb"))
parkinsons_model = pickle.load(open('parkinsons_data.sav', "rb"))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkisons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Enter number of pregnancies:', '2')
    with col2:
        glucose = st.text_input('Enter Glucose Level:', '120')
    with col3:
        blood_pressure = st.text_input('Enter Blood Pressure value:', '70')
    with col1:
        skin_thickness = st.text_input('Skin Thickness value:', '20')
    with col2:
        insulin = st.text_input('Insulin level:', '80')
    with col3:
        BMI = st.text_input('BMI value:', '25.0')
    with col1:
        diabetes_function = st.text_input('Diabetes Pedigree Function Value:', '0.5')
    with col2:
        age = st.text_input('Age of the person:', '35')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[
                int(pregnancies), int(glucose), int(blood_pressure),
                int(skin_thickness), int(insulin), float(BMI),
                float(diabetes_function), int(age)
            ]])
            diab_diagnosis = 'You are diabetic' if diab_prediction[0] == 1 else 'You are not diabetic'
        except Exception as e:
            st.error(f"Error during prediction: {e}")

    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age of the person:', '50')
    with col2:
        sex = st.text_input('Sex of the person (1=Male, 0=Female):', '1')
    with col3:
        cp = st.text_input('Enter number of cp:', '3')
    with col4:
        testbp = st.text_input('Enter testbp:', '120')
    with col1:
        chol = st.text_input('Enter chol value:', '240')
    with col2:
        fbs = st.text_input('Fbs value (1=True, 0=False):', '0')
    with col3:
        restecg = st.text_input('Enter restecg:', '0')
    with col4:
        thalach = st.text_input('Thalach value:', '150')
    with col1:
        exang = st.text_input('Exang Function Value (1=True, 0=False):', '0')
    with col2:
        oldpeak = st.text_input('Enter oldpeak:', '1.0')
    with col3:
        slope = st.text_input('Enter Slope:', '2')
    with col4:
        ca = st.text_input('Enter ca:', '0')
    with col1:
        thal = st.text_input('Enter thal:', '2')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[
                int(age), int(sex), int(cp), int(testbp), int(chol),
                int(fbs), int(restecg), int(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]])
            heart_diagnosis = 'You have Heart Disease' if heart_prediction[0] == 1 else 'You do not have Heart Disease'
        except Exception as e:
            st.error(f"Error during prediction: {e}")

    st.success(heart_diagnosis)


    # Parkinson's Prediction
if selected == 'Parkisons Prediction':
    st.title('Parkinson’s Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)

    # Collecting 22 features from the user
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency', '150')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency', '180')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency', '120')
    with col4:
        MDVP_Jitter = st.text_input('MDVP:Jitter - Frequency perturbation', '0.003')
    with col5:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs) - Absolute frequency variation', '0.00003')
    with col1:
        MDVP_RAP = st.text_input('MDVP:RAP - Relative amplitude perturbation', '0.002')
    with col2:
        MDVP_PPQ = st.text_input('MDVP:PPQ - Five-point period perturbation quotient', '0.0025')
    with col3:
        Jitter_DDP = st.text_input('Jitter:DDP - Average absolute difference of differences', '0.007')
    with col4:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer - Amplitude variation', '0.02')
    with col5:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB) - Decibel amplitude variation', '0.2')
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3 - 3-point amplitude perturbation quotient', '0.01')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5 - 5-point amplitude perturbation quotient', '0.02')
    with col3:
        Shimmer_APQ = st.text_input('Shimmer:APQ - Amplitude perturbation quotient', '0.03')
    with col4:
        Shimmer_DDA = st.text_input('Shimmer:DDA - Average absolute difference of differences for amplitude', '0.01')
    with col5:
        NHR = st.text_input('NHR - Noise-to-Harmonics Ratio', '0.01')
    with col1:
        HNR = st.text_input('HNR - Harmonics-to-Noise Ratio', '22')
    with col2:
        RPDE = st.text_input('RPDE - Recurrence period density entropy', '0.45')
    with col3:
        DFA = st.text_input('DFA - Detrended fluctuation analysis', '0.65')
    with col4:
        Spread1 = st.text_input('Spread1 - Nonlinear fundamental frequency variation', '-5.67')
    with col5:
        Spread2 = st.text_input('Spread2 - Variation of fundamental frequency', '0.25')
    with col1:
        D2 = st.text_input('D2 - Correlation dimension', '3.8')
    with col2:
        PPE = st.text_input('PPE - Pitch period entropy', '0.4')

    # Prediction logic
    park_diagnosis = ''
    if st.button('Parkinson’s Test Result'):
        try:
            # Ensure all inputs are converted correctly to float
            park_prediction = parkinsons_model.predict([[
                float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
                float(MDVP_Jitter), float(MDVP_Jitter_Abs), float(MDVP_RAP),
                float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer),
                float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                float(Shimmer_APQ), float(Shimmer_DDA), float(NHR),
                float(HNR), float(RPDE), float(DFA), float(Spread1),
                float(Spread2), float(D2), float(PPE)
            ]])
            park_diagnosis = 'You have Parkinson’s Disease' if park_prediction[0] == 1 else 'You do not have Parkinson’s Disease'
        except Exception as e:
            st.error(f"Error during prediction: {e}")

    st.success(park_diagnosis)
