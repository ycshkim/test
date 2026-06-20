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

st.subheader("국가유산 종목별 개수")

type_count = df["국가유산종목"].value_counts()

# 상위 5개
top5 = type_count.head(5).copy()

# 기타
etc_count = type_count.iloc[5:].sum()

# 상위 5개 내림차순 정렬
top5 = top5.sort_values(ascending=False)

# 기타를 마지막에 추가
top5.loc["기타"] = etc_count

# DataFrame으로 변환
chart_df = top5.reset_index()
chart_df.columns = ["종목", "개수"]

st.bar_chart(chart_df.set_index("종목"))
