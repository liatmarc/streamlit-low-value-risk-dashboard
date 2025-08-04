
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("dashboard_risk_summary_sample.csv")

st.set_page_config(layout="wide")
st.title("Pediatric Risk of Low-Value Diagnostic Testing")

# Sidebar filters
st.sidebar.header("Filters")
chronic_filter = st.sidebar.selectbox("Chronic Condition", options=["All", "0", "1"])
age_filter = st.sidebar.slider("Age Range", min_value=int(df.age.min()), max_value=int(df.age.max()), value=(1, 17))

# Apply filters
if chronic_filter != "All":
    df = df[df['chronic_condition_flag'] == int(chronic_filter)]
df = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]

# Layout: Histogram and Scatter/Table
col1, col2 = st.columns([1, 2])

# Left column: Histogram
with col1:
    st.subheader("Risk Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(df['predicted_risk'], bins=20, kde=False, ax=ax1, color='skyblue')
    ax1.set_xlabel("Predicted Risk")
    ax1.set_ylabel("Patient Count")
    st.pyplot(fig1)

# Right column: Scatter and Table
with col2:
    st.subheader("Age vs. Predicted Risk")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x='age', y='predicted_risk',
                    hue='chronic_condition_flag', palette="Set2", ax=ax2)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Predicted Risk")
    st.pyplot(fig2)

    st.subheader("Top 10 High-Risk Patients")
    top_patients = df[['patient_id', 'predicted_risk', 'age',
                       'num_prior_tests', 'chronic_condition_flag']]                   .sort_values(by='predicted_risk', ascending=False)                   .head(10)
    st.dataframe(top_patients)

    # Export option
    csv_export = top_patients.to_csv(index=False).encode('utf-8')
    st.download_button("Download Top 10 as CSV", csv_export, "top_high_risk_patients.csv", "text/csv")
