import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()

# 데이터 불러오기
df = pd.read_csv("yc_heritage_detail_enriched.csv")

st.subheader("시군구별 문화재 수")

# 시군구별 문화재 개수 집계
region_count = df["시군구명"].value_counts()

# 그래프 출력
st.bar_chart(region_count)
