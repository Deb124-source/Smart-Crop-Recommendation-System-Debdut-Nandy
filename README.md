# AgriSense AI

An AI-powered crop recommendation system that predicts the most suitable crop based on soil and environmental conditions.

The model analyzes important agricultural parameters such as soil nutrients, temperature, humidity, pH level, and rainfall to recommend the best crop for cultivation.


## Live Demo:

https://agrisense-ai-debdut-nandy.streamlit.app/

## Features

* Crop recommendation using Machine Learning
* Soil and climate based prediction
* XGBoost classification model
* Interactive Streamlit web application
* Real-time crop prediction

## Dataset

The dataset contains agricultural parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

Target variable:

* Crop label

## Machine Learning Workflow

1. Data Collection
2. Data Exploration and Analysis
3. Feature and Target Separation
4. Label Encoding
5. Model Training using XGBoost Classifier
6. Model Evaluation
7. Model Deployment using Streamlit

## Model

Algorithm used:

* XGBoost Classifier

The model learns patterns between soil conditions, climate factors, and crop types to provide suitable recommendations.

## Project Structure

```
AgriSense-AI/

│
├── app.py
├── crop_model.pkl
├── label_encoder.pkl
├── features.json
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

## Installation

Clone the repository:

```
git clone <repository-link>
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run Application

Start the Streamlit application:

```
streamlit run app.py
```

## Application Workflow

User enters:

* Soil nutrient values
* Temperature
* Humidity
* Soil pH
* Rainfall

The trained machine learning model processes the input and recommends the most suitable crop.

## Future Improvements

* Add weather API integration
* Add regional crop recommendation
* Improve prediction confidence display
* Add fertilizer recommendation system

## Author

Debdut Nandy
