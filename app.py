import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정 (반드시 맨 위에 1번만)
st.set_page_config(
    page_title="문화재 훼손 예측",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ 문화재 훼손 예측 및 환경 리포트")
st.divider()

# =========================
# 문화재 데이터
# =========================

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")

st.subheader("문화재 데이터")
st.dataframe(df)

# =========================
# 문화재 위치
# =========================

st.subheader("📍 문화재 위치")

map_df = df[["위도", "경도"]].dropna()
map_df.columns = ["lat", "lon"]

st.map(map_df)

# =========================
# 국가유산 종목별 개수
# =========================

st.subheader("📊 국가유산 종목별 개수")

type_count = df["국가유산종목"].value_counts()

top5 = type_count.head(5).copy()
etc_count = type_count.iloc[5:].sum()

chart_df = pd.DataFrame({
    "종목": top5.index,
    "개수": top5.values
})

chart_df.loc[len(chart_df)] = ["기타", etc_count]

fig = px.bar(
    chart_df,
    x="개수",
    y="종목",
    orientation="h",
    text="개수",
    title="국가유산 종목별 개수"
)

fig.update_layout(
    xaxis_title="문화재 개수",
    yaxis_title="국가유산 종목"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="heritage_type_chart"
)

st.divider()

# =========================
# 영천 환경 리포트
# =========================

st.header("🌎 영천 환경 리포트")

weather = pd.read_csv(
    "data/[2016_2025] yeongcheon_weather_daily.csv"
)

air = pd.read_csv(
    "data/[2019_2025] air_quality.csv"
)

weather["date"] = pd.to_datetime(weather["date"])
air["date"] = pd.to_datetime(air["date"])

env = pd.merge(
    weather,
    air,
    on="date",
    how="inner"
)

# 날짜 선택
selected_date = st.date_input(
    "📅 날짜 선택",
    value=env["date"].max().date()
)

row = env[env["date"].dt.date == selected_date]

if row.empty:
    st.warning("선택한 날짜의 데이터가 없습니다.")
    st.stop()

# 값 추출
temp = row["avg_temperature_c"].iloc[0]
humidity = row["avg_relative_humidity_pct"].iloc[0]
rain = row["daily_precipitation_mm"].iloc[0]
wind = row["avg_wind_speed_ms"].iloc[0]

pm10 = row["pm10"].iloc[0]
pm25 = row["pm25"].iloc[0]
o3 = row["o3"].iloc[0]

# 강수량 결측치 처리
rain_text = (
    "데이터 없음"
    if pd.isna(rain)
    else f"{rain:.1f} mm"
)

# =========================
# 환경 현황 카드
# =========================

st.subheader(f"📋 {selected_date} 환경 현황")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("평균기온", f"{temp:.1f} ℃")

with col2:
    st.metric("습도", f"{humidity:.1f} %")

with col3:
    st.metric("강수량", rain_text)

with col4:
    st.metric("풍속", f"{wind:.1f} m/s")

st.divider()

col5, col6, col7 = st.columns(3)

with col5:
    st.metric("PM10", f"{pm10:.1f}")

with col6:
    st.metric("PM2.5", f"{pm25:.1f}")

with col7:
    st.metric("오존(O₃)", f"{o3:.3f}")

st.divider()

# =========================
# 최근 30일 변화
# =========================

recent = env.sort_values("date").tail(30)

st.subheader("📈 최근 30일 평균기온 변화")

st.line_chart(
    recent.set_index("date")["avg_temperature_c"]
)

st.subheader("📈 최근 30일 PM10 변화")

st.line_chart(
    recent.set_index("date")["pm10"]
)

# =========================
# 환경요소 비교
# =========================

st.subheader("📊 선택 날짜 환경요소 비교")

compare = pd.DataFrame({
    "항목": ["기온", "습도", "풍속"],
    "값": [temp, humidity, wind]
})

st.bar_chart(compare.set_index("항목"))

