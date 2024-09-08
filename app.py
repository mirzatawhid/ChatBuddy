import streamlit as st
from chatbot import get_response

st.title("Mental Health Chatbot")

# Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def send_message():
    user_message = st.session_state.user_input

    # Check for the 'quit' command
    if user_message.lower() == "quit":
        st.write("Chat session ended.")
        st.session_state.chat_history = []  # Clear chat history
        st.stop()  # Stop further execution

    bot_response = get_response(user_message)
    
    # Append user and bot messages to chat history
    st.session_state.chat_history.append(f"You: {user_message}")
    st.session_state.chat_history.append(f"Bot: {bot_response}")
    
    # Clear the input box after sending the message
    st.session_state.user_input = ""

# Display chat history
for message in st.session_state.chat_history:
    st.markdown(message, unsafe_allow_html=True)

# User input text box
st.text_input("Enter your message (type 'quit' to exit):", key="user_input", on_change=send_message)