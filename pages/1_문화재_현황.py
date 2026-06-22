import streamlit as st
import pandas as pd

st.title("📍 문화재 위치")

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")

map_df = df[["위도", "경도"]].dropna()
map_df.columns = ["lat", "lon"]

st.map(map_df)
