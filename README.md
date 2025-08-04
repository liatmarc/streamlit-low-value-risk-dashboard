# streamlit-low-value-risk-dashboard
Interactive dashboard to monitor risk of low-value diagnostic testing in pediatric care
# Pediatric Risk Dashboard: Low-Value Diagnostic Testing

This interactive Streamlit app helps visualize the predicted risk of low-value diagnostic tests in a pediatric population. It is designed to support quality and safety teams in identifying areas of overuse, improving care coordination, and promoting value-based decision-making.

## 🔍 Features

- Filter by **chronic condition** and **age range**
- Visualize:
  - **Predicted risk distribution** (histogram)
  - **Age vs. risk scatter plot**
  - **Top 10 high-risk patients**
- **Export high-risk list** to CSV
- Clean and responsive layout for use by clinical or analytics teams

## 🧪 Simulated Data

The data is simulated and contains the following fields:

| Column | Description |
|--------|-------------|
| `patient_id` | Unique ID for the patient |
| `predicted_risk` | Model-predicted risk score (0–1) |
| `age` | Age in years |
| `num_prior_tests` | Number of prior diagnostic tests |
| `chronic_condition_flag` | Whether the patient has a chronic condition (0 = No, 1 = Yes) |

## 🚀 How to Run Locally

```bash
pip install streamlit pandas seaborn matplotlib
streamlit run streamlit_risk_dashboard_updated.py

