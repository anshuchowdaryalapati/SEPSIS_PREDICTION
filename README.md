# SEPSIS_PREDICTION
Goal of the analysis is the early detection of sepsis using vital signs data.The early prediction of sepsis is potentially life-saving. We will be predicting the % chance of occurrence of sepsis in a person with the reasons stated using laboratory values, vital signs and patient information, in the website.

Summary Report: Prediction of Sepsis Using Vital Signs

**Introduction:**
This report outlines a Sepsis Risk Assessment application that utilizes vital signs data and an XGBoost machine learning model to predict the risk of sepsis in patients. Sepsis is a severe medical condition characterized by a systemic inflammatory response to infection, and early detection is critical for timely intervention.

**Data Source:**
The application uses patient data from a CSV file, which includes vital signs and demographic information.

**Model Training:**
1. The XGBoost machine learning model is used for prediction.
2. The dataset is split into training and testing sets (80% training, 20% testing) to train and evaluate the model.
3. The model is trained with the following parameters:
   - Objective: Binary logistic
   - Evaluation Metric: Logarithmic loss
   - Learning Rate (Eta): 0.1
   - Maximum Depth: 6
   - Subsample: 0.8
   - Column Sample by Tree: 0.8
   - Minimum Child Weight: 3
   - Gamma: 0.1
   - Random Seed: 42

**Input Data:**
Users can input patient information via a Streamlit interface. The following vital signs and demographic information are collected:
- Age
- Gender
- Heart Rate (HR)
- Pulse Oximetry (O2Sat)
- Temperature
- Systolic Blood Pressure (SBP)
- Mean Arterial Pressure (MAP)
- Diastolic Blood Pressure (DBP)
- Respiration Rate (Resp)
- End Tidal Carbon Dioxide (EtCO2)
- Fraction of Inspired Oxygen (FiO2)
- Glucose Serum Glucose
- Potassium
- Hematocrit (Hct)
- Hemoglobin (Hgb)

**Sepsis Risk Assessment:**
1. Users input patient data and submit it.
2. The model predicts the probability of sepsis based on the input data.
3. The application displays the risk assessment result:
   - If the probability is less than 0.4, it indicates a minor chance of sepsis.
   - If the probability is greater than or equal to 0.4, it indicates a major chance of sepsis.

**Sepsis Risk Factors:**
The application also assesses the severity of sepsis risk factors based on vital signs. Each factor is categorized into "Low," "Mild," or "Severe" based on predefined severity ranges.

**Conclusion:**
This Sepsis Risk Assessment application provides a user-friendly interface for predicting the risk of sepsis in patients based on their vital signs and demographic information. It can aid healthcare professionals in identifying individuals at risk of sepsis and taking appropriate measures for early intervention.
