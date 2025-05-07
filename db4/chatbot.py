import streamlit as st
import ollama


def init_session_state(keys: dict):
    for key, value in keys.items():
        if key not in st.session_state:  # 키에 어떤 값도 없는건지?
            st.session_state[key] = value


def chat_message_user(prompt: str) -> dict:  # return str 문자형 나올때 (return) 자료형이 딕셔너리
    with st.chat_message("user"):
        st.markdown(prompt)
    return dict(role="user", content=prompt)


def chat_message_llm(role: str, model: str, messages: list) -> dict:
    with st.chat_message(role):
        with st.spinner("답변은 준비중입니다."):
            response = ollama.chat(model=model, messages=messages)
            msg_llm = response.get("message", {})
            print(msg_llm)
            st.markdown(msg_llm["content"])
    return msg_llm


if __name__ == "__main__":
    st.set_page_config(layout="wide")  # 기본설정을 해주는 문법
    st.title("🥲 그만 물어보면 안되겠니?")

    init_session_state(dict(msgs=[]))  # {msgs:[]}
    msgs = st.session_state["msgs"]

    for row in msgs:
        with st.chat_message(row["role"]):
            st.markdown(row["content"])

    if prompt := st.chat_input("여기에 대화를 입력하세요!"):
        msg_user = chat_message_user(prompt)
        msgs.append(msg_user)
        # ["오즈코딩스쿨이란?"]
        msg_llm = chat_message_llm("assistant", "gemma2:9b", msgs)
        msgs.append(msg_llm)