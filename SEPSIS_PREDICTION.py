import pandas as pd
import numpy as np
import xgboost as xgb
import streamlit as st
from sklearn.model_selection import train_test_split

# Load the XGBoost model
data = pd.read_csv("C:\\Users\\91909\\Downloads\\nms.csv")

X = data.drop("SepsisLabel", axis=1).values
y = data["SepsisLabel"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'eta': 0.1,
    'max_depth': 6,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'min_child_weight': 3,
    'gamma': 0.1,
    'seed': 42
}
model = xgb.train(params, dtrain, num_boost_round=100)

column_names = ['Age', 'Gender','HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'FiO2', 'Glucose','Potassium','Hct','Hgb']

# Define severity ranges and categories
severity_ranges = {
    'etco2': [(0, 25), (25, 30)],
    'hr': [(90, 100), (100, 140)],
    'spo2': [(90, 94), (85, 89)],
    'temp': [(96.8, 100.4), (100.4, 104)],
    'sbp': [(90, 119)],
    'map': [(65, 100)],
    'dbp': [(50, 80)],
    'resp_rate': [(12, 20), (20, 40)],
    'potassium': [(0, 3.5), (3.5, 4.5)],
    'hgb': [(12, 14), (10, 12)],
    'fio2': [(21, 30), (30, 50)],
    'hct': [(0, 35), (35, 45)]
}

sepsis_severity = {
    0: "Low",
    1: "Mild",
    2: "Severe"
}
def get_severity_range(value, ranges):
    for idx, (low, high) in enumerate(ranges):
        if low <= value <= high:
            return idx
    return len(ranges)

def main():
    st.title("Sepsis Risk Assessment")

    st.subheader("Enter Patient Information:")
    age = st.number_input("Age:")
    gender = st.radio("Gender:", ("Male", "Female"))
    hr = st.number_input("Heart Rate (beats per minute):")
    o2sat = st.number_input("Pulse Oximetry (%):")
    temp = st.number_input("Temperature (Deg C):")
    sbp = st.number_input("Systolic BP (mm Hg):")
    map_ = st.number_input("Mean Arterial Pressure (mm Hg):")
    dbp = st.number_input("Diastolic BP (mm Hg):")
    resp = st.number_input("Respiration Rate (breaths per minute):")
    etco2 = st.number_input("End Tidal Carbon Dioxide (mm Hg):")
    fio2 = st.number_input("Fraction of inspired oxygen (%):")
    glucose = st.number_input("Glucose Serum glucose (mg/dL):")
    potassium = st.number_input("Potassium (mmol/L):")
    hct = st.number_input("Hematocrit (%):")
    hgb = st.number_input("Hemoglobin (g/dL):")

    submit_button = st.button("Submit")

    if submit_button:
        input_data = np.array([[age, hr, o2sat, temp, sbp, map_, dbp, resp, etco2, fio2, glucose, potassium, hct, hgb]])
        input_dmatrix = xgb.DMatrix(input_data)
        probability = model.predict(input_dmatrix)[0]

        st.subheader("Sepsis Risk Assessment Result:")
        if probability < 0.4:
            st.write(f"Probability of Sepsis: {probability * 100:.2f}% - MINOR CHANCE OF GETTING INFECTED WITH SEPSIS")
        else:
            st.write(f"Probability of Sepsis: {probability * 100:.2f}% - MAJOR CHANCE OF INFECTED WITH SEPSIS")


    input_data = np.array([[age, hr, o2sat, temp, sbp, map_, dbp, resp, etco2, fio2, glucose, potassium, hct, hgb]])

    # Calculate sepsis probability
    input_dmatrix = xgb.DMatrix(input_data)
    probability = model.predict(input_dmatrix)[0]



    sepsis_factors = {
        'etco2': get_severity_range(etco2, severity_ranges['etco2']),
        'hr': get_severity_range(hr, severity_ranges['hr']),
        'spo2': get_severity_range(o2sat, severity_ranges['spo2']),
        'temp': get_severity_range(temp, severity_ranges['temp']),
        'sbp': get_severity_range(sbp, severity_ranges['sbp']),
        'map': get_severity_range(map_, severity_ranges['map']),
        'dbp': get_severity_range(dbp, severity_ranges['dbp']),
        'resp_rate': get_severity_range(resp, severity_ranges['resp_rate']),
        'potassium': get_severity_range(potassium, severity_ranges['potassium']),
        'hgb': get_severity_range(hgb, severity_ranges['hgb']),
        'fio2': get_severity_range(fio2, severity_ranges['fio2']),
        'hct': get_severity_range(hct, severity_ranges['hct'])
    }

    st.subheader("SEPSIS RISK FACTORS:")
    for factor, severity in sepsis_factors.items():
        st.write(f"{factor.upper()}: {sepsis_severity[severity]}")

if __name__ == '__main__':
    main()
