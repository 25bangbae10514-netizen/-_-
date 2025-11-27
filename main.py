import streamlit as st
import random

st.title("🔢 숫자 비교 게임")
st.write("내가 비밀리에 숫자 하나를 골라두었어. 네가 입력한 숫자와 비교해서 알려줄게!")

# 세션 상태에 비밀 숫자 저장 (앱 재실행해도 유지)
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 1000)  # 범위를 바꾸고 싶으면 이 부분 변경

# 사용자 입력
user_input = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

# 확인 버튼
if st.button("결과 확인"):
    secret = st.session_state.secret_number

    if user_input < secret:
        st.info("👉 UP")
    elif user_input > secret:
        st.info("👉 DOWN")
    else:
        st.success("🎉 정답! 숫자가 같아!")

# 숫자 리셋 버튼 (원하면 삭제 가능)
if st.button("비밀 숫자 다시 선택하기"):
    st.session_state.secret_number = random.randint(1, 1000)
    st.warning("🔄 새로운 숫자를 골랐어!")
