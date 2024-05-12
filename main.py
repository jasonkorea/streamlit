from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

# Streamlit 앱의 제목 설정
st.title(':sunglasses: :blue_book: 인공지능 시인')

# 시의 주제 입력 받기
input_title = st.text_input("시의 주제를 제시해주세요.")

# 시 생성 요청 버튼
if st.button("시 생성"):
    with st.spinner("시를 작성 중입니다..."):
        try:
            # ChatOpenAI 인스턴스 생성 및 시 생성 요청
            apiKey = os.getenv("OPENAI_API_KEY")
            llm = ChatOpenAI(api_key=apiKey, model="gpt-4-turbo")
            result = llm.invoke(f"시제가 '{input_title}'이고 라임과 펀치라인이 엄격한 시를 써줘.")
            st.write(result.content)  # 결과 출력
        except Exception as e:
            st.error("시를 생성하는 데 실패했습니다. 오류: " + str(e))
else:
    st.write("주제를 입력하고 버튼을 눌러주세요.")