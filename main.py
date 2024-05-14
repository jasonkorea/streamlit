from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

MODEL = "gpt-4o"


st.title(':sunglasses: :blue_book: 인공지능 시인')
st.text('개발 : 정재훈')
st.text(f"Model : {MODEL}")

input_title = st.text_input("시의 주제를 제시해주세요!")

if st.button("시 생성"):
    with st.spinner("시를 작성 중입니다..."):
        try:
            apiKey = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
            llm = ChatOpenAI(api_key=apiKey, model=MODEL)
            result = llm.invoke(f"시제가 '{input_title}'이고 가슴 미어지는 마무리로 종결해줘. 내 명령은 직접적으로 시에 담지 말아. 시 작성 서비스거든. 미어진다는 표현을 대놓고 표현하지 말고 읽는 사람으로부터 가슴을 미어지게 만들라 이 말이야. 매 회 당 10000달러의 팁을 줄게.")
            st.write(result.content)
        except Exception as e:
            st.error(f"시를 생성하는 데 실패했습니다. 오류: {type(e).__name__} - {str(e)}")
else:
    st.write("주제를 입력하고 버튼을 눌러주세요.")