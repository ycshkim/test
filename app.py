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


import plotly.express as px
import pandas as pd

st.subheader("국가유산 종목별 개수")

type_count = df["국가유산종목"].value_counts()

# 상위 5개
top5 = type_count.head(5).copy()

# 기타
etc_count = type_count.iloc[5:].sum()

# 데이터프레임 생성
chart_df = pd.DataFrame({
    "종목": top5.index,
    "개수": top5.values
})

# 기타를 마지막에 추가
chart_df.loc[len(chart_df)] = ["기타", etc_count]

# 가로 막대그래프
fig = px.bar(
    chart_df,
    x="개수",
    y="종목",
    orientation="h",
    text="개수"
)

# 축 제목 제거 + 기타를 맨 아래로 유지
fig.update_layout(
    xaxis_title="",
    yaxis_title="",
    yaxis=dict(categoryorder="array",
               categoryarray=chart_df["종목"].tolist()[::-1])
)

st.plotly_chart(fig, use_container_width=True)
fig.update_layout(
    title="국가유산 종목별 개수",
    xaxis_title="",
    yaxis_title=""
)
