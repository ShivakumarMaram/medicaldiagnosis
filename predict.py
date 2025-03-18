
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("C:/Users/SHIVA-KUMAR/OneDrive/Desktop/medical/trained_model.sav",'rb'))

heart_disease_model = pickle.load(open("C:/Users/SHIVA-KUMAR/OneDrive/Desktop/medical/heart_disease_model.sav",'rb'))






# Adding Background Image
background_image_url = "https://th.bing.com/th/id/OIP.bbBnAVdPK-dM6hin7CQL5gHaD-?w=280&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)




#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease prediction ',
                           
                           ['Diabetics prediction',
                            'Heart Diesease prediction',],
                           
                           icons = ['person','heart'],
                           
                            default_index = 0)
    
    
#Diabetes prediction page
if (selected == 'Diabetics prediction'):
    
    #page title
    st.title('Diabetics prediction')
    
    #getting the input data from user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the person')
    
    
    
    # code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
    st.success(diab_diagnosis)
    
    
    
    
 
# Heart Disease prediction page
if (selected == 'Heart Diesease prediction'): 
    
    #page title
    st.title('Heart Diesease prediction')
    
    #getting the input data from user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('sex')
        
    with col3:
        cp = st.text_input('chest pain types')
        
    with col1:
        rest_bp = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum cholestral im mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood sugar>120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate achived')
    
    with col3:
        exang = st.text_input('Exercise Induced by angina')
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise St segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by floursopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversalble defect')
        
        
    
    # code for prediction
    # code for prediction
    heart_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Heart Diesease Test Result'):
        try:
            Age = float(Age)
            sex = float(sex)
            cp = float(cp)
            rest_bp = float(rest_bp)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)
        
            heart_prediction = heart_disease_model.predict([[Age, sex, cp, rest_bp, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
            
            else:
                heart_diagnosis = 'The person is Not have any heart disease'
            st.success(heart_diagnosis)
        except ValueError:
            st.error("please enter valid numeric values")
             