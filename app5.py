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

# Function to get career psychology insights
def get_career_psychology_insights():
    model = initialize_model()
    prompt = """
    Provide insights on career psychology for students and job seekers. Include:
    1. Understanding personal strengths and weaknesses
    2. Dealing with career uncertainty
    3. Building resilience in job search
    4. Overcoming imposter syndrome
    5. Work-life balance expectations
    Format the response in markdown with clear headings and bullet points.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit App
def main():
    st.title("🧠 Career Psychology Insights")

    if st.button("Get Career Psychology Insights"):
        with st.spinner("Generating insights..."):
            insights = get_career_psychology_insights()
            st.markdown(insights)

if __name__ == "__main__":
    main()
