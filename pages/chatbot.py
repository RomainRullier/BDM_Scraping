import streamlit as st
import random
import time
from classes.Processor import TextProcessor

processor = TextProcessor(key=str(st.secrets["openai_key"])

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    print(message)
    with st.chat_message(message["role"]):
        if message['type'] == 'text':
            st.markdown(message["content"])
        elif message['type'] == 'image':
            st.image(message["content"])
        elif message['type'] == 'code':
            st.code(message["content"])
        elif message['type'] == 'json':
            st.json(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, "type": 'text'})
    # Display user message in chat message container
    is_code_prompt = prompt.startswith('/code')
    with st.chat_message("user"):
        if is_code_prompt:
            st.code(prompt.replace('/code', '').strip())
        else:
            st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        assistant_response = processor.prompt(prompt)
        if assistant_response['type'] == 'text':
            message_placeholder.markdown(assistant_response['content'])
        elif assistant_response['type'] == 'image':
            message_placeholder.image(assistant_response['content'])
        elif assistant_response['type'] == 'code':
            message_placeholder.code(assistant_response['content'])
        elif assistant_response['type'] == 'json':
            message_placeholder.json(assistant_response['content'])
        full_response = assistant_response['content']
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response, "type": assistant_response['type']})