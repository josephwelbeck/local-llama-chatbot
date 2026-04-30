import streamlit as st
import ollama

# Set the page configuration
st.set_page_config(page_title="My Local AI", page_icon="🤖")

st.title("🤖 Local Llama Chatbot")
st.caption("Running locally with Llama 3.2 - No Data Leaves This PC!")

# Memory
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you today?"}]

# Display history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Interaction loop
if prompt := st.chat_input("What is on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model='llama3.2',
            messages=st.session_state.messages,
            stream=True,
        )

        for chunk in stream:
            if chunk['message']['content']:
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
