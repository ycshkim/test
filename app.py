import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="문화재 훼손 예측")

st.title("문화재 훼손 예측")
st.divider()

# 데이터 불러오기
df = pd.read_csv("yc_heritage_detail_enriched.csv")

# 데이터 미리보기
with st.expander("데이터 보기"):
    st.dataframe(df)

# ------------------
# 시군구별 문화재 수
# ------------------
st.subheader("📍 시군구별 문화재 분포")

region_count = (
    df["시군구명"]
    .value_counts()
    .reset_index()
)

region_count.columns = ["시군구", "개수"]

fig1 = px.bar(
    region_count,
    x="시군구",
    y="개수",
    text="개수",
    title="시군구별 문화재 수"
)

st.plotly_chart(fig1, use_container_width=True)

# ------------------
# 시대별 문화재 수
# ------------------
st.subheader("🏺 시대별 문화재 분포")

era_count = (
    df["시대"]
    .value_counts()
    .head(10)
    .reset_index()
)

era_count.columns = ["시대", "개수"]

fig2 = px.pie(
    era_count,
    names="시대",
    values="개수",
    title="시대별 문화재 비율"
)

st.plotly_chart(fig2, use_container_width=True)
