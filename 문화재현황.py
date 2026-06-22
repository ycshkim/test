import streamlit as st
import pandas as pd

st.title("📊 문화재 현황")

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")

st.dataframe(df)
