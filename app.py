import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="문화재 훼손 예측"
)

st.title("🏛️ 문화재 훼손 예측")
st.divider()

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")

# 원본 데이터
st.subheader("원본 데이터")
st.dataframe(df)

# 국가유산 종목별 개수
st.subheader("국가유산 종목별 개수")

type_count = df["국가유산종목"].value_counts().reset_index()
type_count.columns = ["종목", "개수"]

fig1 = px.bar(
    type_count,
    x="종목",
    y="개수",
    title="국가유산 종목별 개수"
)

st.plotly_chart(fig1, use_container_width=True)

# 시대별 문화재 분포
st.subheader("시대별 문화재 분포")

era_count = df["시대"].value_counts().head(10).reset_index()
era_count.columns = ["시대", "개수"]

fig2 = px.bar(
    era_count,
    x="시대",
    y="개수",
    title="시대별 문화재 수"
)

st.plotly_chart(fig2, use_container_width=True)

# 시군구별 문화재 개수
st.subheader("시군구별 문화재 개수")

region_count = df["시군구명"].value_counts().reset_index()
region_count.columns = ["시군구", "개수"]

fig3 = px.bar(
    region_count,
    x="시군구",
    y="개수",
    title="시군구별 문화재 수"
)

st.plotly_chart(fig3, use_container_width=True)

# 문화재 위치 지도
st.subheader("문화재 위치")

fig4 = px.scatter_mapbox(
    df,
    lat="위도",
    lon="경도",
    hover_name="문화재명(국문)",
    color="국가유산종목",
    zoom=7,
    height=600
)

fig4.update_layout(
    mapbox_style="open-street-map",
    margin=dict(l=0, r=0, t=30, b=0)
)

st.plotly_chart(fig4, use_container_width=True)
