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


import matplotlib.pyplot as plt

st.subheader("국가유산 종목별 개수")

type_count = df["국가유산종목"].value_counts()

# 상위 5개 + 기타
top5 = type_count.head(5)
top5["기타"] = type_count.iloc[5:].sum()

fig, ax = plt.subplots(figsize=(8, 4))

ax.barh(top5.index, top5.values)

ax.set_xlabel("개수")
ax.set_ylabel("국가유산 종목")
ax.set_title("국가유산 종목별 개수")

st.pyplot(fig)
