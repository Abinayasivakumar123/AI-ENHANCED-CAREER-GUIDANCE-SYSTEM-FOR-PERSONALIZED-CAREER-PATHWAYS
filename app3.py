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

# Function to get skill recommendations and learning resources
def get_skill_recommendations(skill):
    model = initialize_model()
    prompt = f"""
    For the skill '{skill}', provide:
    1. Best online learning platforms (with direct links)
    2. Free resources (with direct links)
    3. Paid courses (with direct links)
    4. Estimated time to learn
    5. Career opportunities
    Format the response in markdown with clear headings and bullet points.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit App
def main():
    st.title("🎯 Skill Development Resources")

    skill = st.text_input("Enter a skill you want to learn:")
    
    if skill and st.button("Get Resources"):
        with st.spinner("Finding learning resources..."):
            recommendations = get_skill_recommendations(skill)
            st.markdown(recommendations)

if __name__ == "__main__":
    main()
