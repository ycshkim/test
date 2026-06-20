import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="문화재 훼손 예측"
)
st.title("문화재 훼손 예측")
st.divider()
df=pd.read_csv("data/yc_heritage_detail_enriched.csv")
st.dataframe(df)


st.subheader("문화재 위치")

map_df = df[["위도", "경도"]].dropna()
map_df.columns = ["lat", "lon"]

st.map(map_df)
