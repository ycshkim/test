import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
  page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()





df = pd.read_csv("yc_heritage_detail_enriched.csv")

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

top = df['시군구명'].value_counts()

top.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title('시군구별 문화재 수')
plt.xlabel('시군구')
plt.ylabel('문화재 수')
plt.tight_layout()
plt.show()
