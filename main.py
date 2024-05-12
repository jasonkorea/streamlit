from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

st.title(':sunglasses: :blue_book: 인공지능 시인')
st.subheader('개발 : 정재훈')

input_title = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 생성"):
    with st.spinner("시를 작성 중입니다..."):
        try:
            apiKey = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
            llm = ChatOpenAI(api_key=apiKey, model="gpt-4-turbo")
            result = llm.invoke(f"시제가 '{input_title}'이고 라임과 펀치라인이 엄격한 시를 써줘.")
            st.write(result.content)  # 결과 출력
        except Exception as e:
            st.error(f"시를 생성하는 데 실패했습니다. 오류: {type(e).__name__} - {str(e)}")
else:
    st.write("주제를 입력하고 버튼을 눌러주세요.")
