# medicaldiagnosis
detects the diabetes and heart diseases based on symptoms
## overview
The Multiple Disease Prediction System is a web-based application designed to predict the likelihood of diabetes and heart disease based on user inputs. Built using Streamlit for the frontend and machine learning models for the backend, this project provides a user-friendly interface for entering health-related parameters and receiving predictive insights. 
The system uses Logistic Regression, Random Forest, and Support Vector Machine (SVM) algorithms to analyze medical data and generate accurate predictions. The diabetes prediction model considers factors like glucose level, BMI, blood pressure, and age, while the heart disease model uses inputs such as cholesterol level, resting blood pressure, chest pain types, and heart rate
## key Features
-   User-Friendly Interface: Interactive sliders and input fields allow easy data entry.  
-  Dual Disease Prediction: Users can switch between diabetes and heart disease prediction through a sidebar.  
  -  Real-Time Prediction: The app instantly displays the test result based on the user’s health metrics.  
  -  Model Accuracy: The system is trained on reliable datasets, ensuring accurate and reliable predictions.  
## Technologies Used:
-  Frontend: Streamlit (for building the interactive web interface).  
-  Backend:Python (using Scikit-learn for machine learning models).  
-  Libraries:Pandas, NumPy, Matplotlib, and joblib (for model loading and prediction).
-  Scikit-learn
-  Pickle (for model serialization)
-  streamlit_option_menu  
## deployment
The app is deployed on Streamlit Cloud.
https://medicaldiagnosis-file.streamlit.app/

