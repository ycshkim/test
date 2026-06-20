import streamlit as st
import pandas as pd
import plotly.express as px
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

st.subheader("국가유산 종목별 개수")
type_count = df["국가유산종목"].value_counts()
# 상위 5개
top5 = type_count.head(5).copy()
# 기타
etc_count = type_count.iloc[5:].sum()
# 기타를 마지막에 추가
top5["기타"] = etc_count
# DataFrame 변환
chart_df = top5.reset_index()
chart_df.columns = ["종목", "개수"]
# 가로 막대그래프
fig = px.bar(
    chart_df,
    x="개수",
    y="종목",
    orientation="h",
    title="국가유산 종목별 개수"
)
# 큰 값이 위에 오도록
fig.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)
