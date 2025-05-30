import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
def initialize_model():
    return genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS (Removed background styling)
st.markdown("""
<style>
    .chat-message {
        padding: 1rem;
            
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        color: white;
    }
    .user-message {
        background-color: rgba(25, 25, 112, 0.7);
    }
    .bot-message {
        background-color: rgba(178, 34, 34, 0.7);
    }
    .stButton>button {
        background-color: #fdbb2d;
        color: #1a2a6c;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.2);
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Main Chat App
def main():
    st.title("🚀 Career Chat Assistant")

    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.subheader("💬 Career Chat Assistant")

    user_input = st.text_input("Ask anything about careers, skills, or job roles:")

    if st.button("Send"):
        if user_input:
            model = initialize_model()
            prompt = f"""
            You are a career development assistant. Provide helpful advice about:
            - Career paths
            - Job roles and responsibilities
            - Required skills
            - Industry trends
            - Professional development

            Question: {user_input}
            """
            response = model.generate_content(prompt)
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("bot", response.text))

    # Display chat history
    for role, text in st.session_state.chat_history:
        div_class = "user-message" if role == "user" else "bot-message"
        st.markdown(f'<div class="chat-message {div_class}">{text}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
