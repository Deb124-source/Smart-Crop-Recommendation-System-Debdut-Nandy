import streamlit as st
import numpy as np
import joblib
import json


# -----------------
# Page Config
# -----------------

st.set_page_config(

page_title="Crop Recommendation AI",

page_icon="",

layout="centered"

)



# -----------------
# Load Model
# -----------------

model = joblib.load(
    "crop_model.pkl"
)


encoder = joblib.load(
    "label_encoder.pkl"
)


with open(
    "features (1).json"
) as f:

    features=json.load(f)



# -----------------
# UI
# -----------------

st.title(
"AgriSense AI"
)


st.subheader(
"Smart Agriculture Assistant"
)


st.write(
"Enter soil and climate conditions to recommend the best crop."
)



col1,col2 = st.columns(2)



with col1:

    N = st.number_input(
        "Nitrogen (N)",
        0,
        150,
        50
    )


    P = st.number_input(
        "Phosphorus (P)",
        0,
        150,
        50
    )


    K = st.number_input(
        "Potassium (K)",
        0,
        150,
        50
    )


    temperature = st.number_input(
        "Temperature",
        value=25.0
    )


with col2:


    humidity = st.number_input(
        "Humidity",
        value=70.0
    )


    ph = st.number_input(
        "Soil pH",
        value=6.5
    )


    rainfall = st.number_input(
        "Rainfall",
        value=100.0
    )



if st.button(
"🌾 Recommend Crop"
):


    data = np.array([

        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall

    ]).reshape(1,-1)



    prediction = model.predict(
        data
    )


    crop = encoder.inverse_transform(
        prediction
    )[0]



    st.success(

        f"Recommended Crop:  {crop.upper()}"

    )
