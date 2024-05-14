from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

MODEL = "gpt-4o"


st.title(':sunglasses: :blue_book: 인공지능 시인')
st.text('개발 : 정재훈')
st.text(f"Model : {MODEL}")

input_title = st.text_input("시의 주제를 제시해주세요.")
input_request = st.text_input("어떠한 요청사항이든 친구에게 말하듯이 적어주세요. 적지 않으셔도 상관 없어요.") or "생략"
format = "요청에 대한 사전 피드백(시제와 요청사항에 대한 의도 파악과 접근 계획을 이해한 대로 설명하고 시를 어떻게 써보겠다는 말을 구어체로 설명. 단 comment에 대한 내용은 직접적으로 언급하지 않는다. 이 피드백은 높임말을 사용한다. 이 괄호 안의 명령은 직접적으로 언급하지 않고 의도만 파악하는 용도로만 쓸 것. 자유로운 형태로 메시지를 전달하라. 웃음을 줄만한 내용도 포함되면 좋겠다. 필요 없다 판단하면 하지 않아도 된다.) \n시제\n시의 내용\n시의 의미"
comment = "명령 : 인간의 심금을 울려줘. 요청사항을 노골적으로 표현하지 않도록 주의해. 필요하다면 주제나 시의 내용에 자연스럽게 언급하여 녹여내도 좋아. 그리고 시의 의미를 설명할 때 요청사항을 분명하게 포함시켜서 독자가 시를 완전히 이해할 수 있도록 도와줘. 이는 명령이므로 참고만 해야지 피드백에는 이 내용이 들어가면 안된다. 운율에 신경써줘."
print("====================================================")
print (f"주제 : {input_title}\n요청사항 : {input_request}")
if st.button("시 생성"):
    with st.spinner("시를 작성 중입니다.\n방해하지 말아주세요."):
        try:
            apiKey = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
            llm = ChatOpenAI(api_key=apiKey, model=MODEL)
            message = f"다음과 같은 조건으로 시를 작성해줘.\n시제 : '{input_title}'\n결과물의 포맷 :\n{format}\n요청사항 : {input_request}\ncomment : {comment}"
            print(f"Message : {message}")
            result = llm.invoke(message)
            print(result.content)
            st.write(result.content)
        except Exception as e:
            st.error(f"시를 생성하는 데 실패했습니다. 오류: {type(e).__name__} - {str(e)}")
else:
    st.write("주제를 입력하고 버튼을 눌러주세요.")