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

# 나머지는 기타로 묶기
etc_count = type_count.iloc[5:].sum()

# 데이터프레임 생성
chart_df = pd.DataFrame({
    "종목": top5.index,
    "개수": top5.values
})

# 기타를 마지막에 추가
chart_df.loc[len(chart_df)] = ["기타", etc_count]

# 가로 막대그래프 생성
fig = px.bar(
    chart_df,
    x="개수",
    y="종목",
    orientation="h",
    text="개수",
    title="국가유산 종목별 개수"
)

# 축 제목 및 순서 설정
fig.update_layout(
    xaxis_title="문화재 개수",
    yaxis_title="국가유산 종목"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="heritage_type_chart"
)





import streamlit as st
import pandas as pd

# 데이터 불러오기
weather = pd.read_csv("data/yeongcheon_weather_daily.csv")
air = pd.read_csv("data/air_quality.csv")

# 날짜 형식 통일
weather["date"] = pd.to_datetime(weather["date"])
air["date"] = pd.to_datetime(air["date"])

# 병합
env = pd.merge(weather, air, on="date", how="inner")

# 날짜 선택
selected_date = st.date_input(
    "날짜 선택",
    value=env["date"].max().date()
)

# 선택 날짜 데이터
row = env[env["date"].dt.date == selected_date]

if not row.empty:

    st.subheader(f"📅 {selected_date} 환경 데이터")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "평균기온",
            f"{row['avg_temperature_c'].iloc[0]:.1f}℃"
        )

    with col2:
        st.metric(
            "습도",
            f"{row['avg_relative_humidity_pct'].iloc[0]:.1f}%"
        )

    with col3:
        st.metric(
            "강수량",
            f"{row['daily_precipitation_mm'].iloc[0]:.1f} mm"
        )

    with col4:
        st.metric(
            "풍속",
            f"{row['avg_wind_speed_ms'].iloc[0]:.1f} m/s"
        )

    st.divider()

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("PM10", row["pm10"].iloc[0])

    with col6:
        st.metric("PM2.5", row["pm25"].iloc[0])

    with col7:
        st.metric("오존(O₃)", row["o3"].iloc[0])

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
