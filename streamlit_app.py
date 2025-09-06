import streamlit as st
import pandas as pd
from datetime import date

# 1. 텍스트 작성하기
st.title("밥묵자🍚")

# 2. 웹에 게시된 csv파일 불러오기
url = "https://github.com/teacher188-netizen/blank-app/blob/main/meals_data.csv" + "?raw=true"
df = pd.read_csv(url, encoding='cp949')
st.dataframe(df)

# 3. 데이터 대시보드 만들기
st.write("오늘의 메뉴를 표 형태로 확인할 수 있어요.")

# 오늘 날짜 불러오기
dt = str(date.today())
st.write("오늘 날짜:", dt)

today_row = df.loc[df['급식일자'] == dt]
st.write(today_row)  # 오늘 날짜에 해당하는 행 출력

# metric 활용하기
if not today_row.empty:
    st.write("metric으로 통계 정보를 전광판 형태로 시각화할 수 있어요.")
    st.title(today_row['요리명'].item())
    st.metric("오늘의 메뉴", today_row['요리명'].item())

    # metric 열 구성하기
    a, b = st.columns(2)
    a.metric("칼로리", today_row['칼로리정보(Kcal)'].item(),
             1600 - today_row['칼로리정보(Kcal)'].item())
    b.metric("탄수화물", today_row['탄수화물(g)'].item())

# 4. 차트로 데이터 시각화하기
# 4-1. 지도 만들기
map_data = pd.DataFrame({
    'lat': [37.485475, 37.497539, 37.498014],
    'lon': [126.501083, 126.486135, 126.569858],
    'school': ['인천영종고', '인천공항고', '인천중산고'],
    'students': [923, 662, 1109]
})

st.map(map_data, size="students")

# 4-2. 선 그래프 만들기
st.line_chart(df, x='급식일자', y=['칼로리정보(Kcal)', '탄수화물(g)'])

# 4-3. 막대 그래프 만들기
st.bar_chart(df, x='급식일자', y='칼로리정보(Kcal)', color='급식일자', horizontal=True)

# 5. 다양한 입력 기능 (form)
with st.form("급식의견받아요"):
    d = st.date_input("날짜를 선택할 수 있는 입력폼")
    a = st.selectbox("항목 중 하나를 선택할 수 있는 입력폼", ["월", "화", "수", "목", "금"])
    b = st.text_input("주관식 입력폼", placeholder="placehoder에 들어가는 값이 힌트가 됩니다.")
    c = st.slider("슬라이더를 조정해서 값을 선택하는 입력폼", 1, 5)

    submitted = st.form_submit_button("제출")

# 제출 내용 확인
if submitted:
    st.write(f"""
    with st.form 안에 들어있는 변수를 중괄호 안에 넣으면 변수와 문자를 함께 출력할 수 있어요.\n
    날짜: {d}
    요일: {a}
    의견: {b}
    점수: {c}
    """)
