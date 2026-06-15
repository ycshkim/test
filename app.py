import streamlit as st
import pandas as pd

st.title("문화재 훼손 예측")

df = pd.read_csv("yc_heritage_detail_enriched.csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    region_count = df["시군구명"].value_counts()

    st.subheader("시군구별 문화재 수")
    st.bar_chart(region_count)
