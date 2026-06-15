import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

df["국가유산종목"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")
st.pyplot(fig)


