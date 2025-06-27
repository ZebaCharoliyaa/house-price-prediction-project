
# 🏠 House Price Prediction

A machine learning project to predict house prices using various features such as square footage, overall quality, number of bathrooms, and year built.

---

## 📌 Problem Statement

Accurately estimating house prices is crucial for real estate businesses, buyers, and sellers. This project builds a regression model that predicts housing prices based on historical data from the Ames Housing dataset.

---

## 📂 Project Structure
house-price-prediction/
│
├── data/ # Raw dataset
│ └── train.csv
│
├── model/ # Trained model and scaler
│ ├── house_model.pkl
│ └── scaler.pkl
│
├── notebook/ # Main ML code
│ └── house_price_prediction.ipynb
│
├── dashboard/ # Streamlit app
│ └── app.py
│
├── reports/ # Final report and presentation
│ ├── project_report.pdf
│ └── presentation.pptx
│
├── README.md # Project overview (this file)
├── requirements.txt # Python dependencies


---

## 🔍 Features Used

- `OverallQual` – Overall material and finish quality  
- `GrLivArea` – Above ground living area (sq ft)  
- `GarageCars` – Garage capacity  
- `TotalBsmtSF` – Basement size (sq ft)  
- `FullBath` – Full bathrooms  
- `YearBuilt` – Year of construction  

---

## 📊 Techniques Used

- Linear Regression  
- Feature Scaling (`StandardScaler`)  
- Data Cleaning & EDA  
- Model Evaluation (R² Score, RMSE)  
- Streamlit Dashboard for deployment  

---
🙋‍♀️ Developed By
Zeba Charoliya

## 🚀 How to Run Locally

1. Clone this repo:
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

##Install dependencies:

pip install -r requirements.txt


##Run the Streamlit app:

cd dashboard
streamlit run app.py


