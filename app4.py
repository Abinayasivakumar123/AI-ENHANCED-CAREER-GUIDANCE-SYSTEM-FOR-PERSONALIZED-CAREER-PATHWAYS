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

# Function to search jobs
def search_jobs(query, location):
    linkedin_url = f"https://www.linkedin.com/jobs/search?keywords={query}&location={location}"
    naukri_url = f"https://www.naukri.com/jobs-in-{location}?keyword={query}"
    return linkedin_url, naukri_url

# Function to get job search tips
def get_job_search_tips(job_title):
    model = initialize_model()
    prompt = f"""
    Provide job search tips and interview preparation advice for the role of {job_title}.
    Include:
    1. Key skills required
    2. Common interview questions
    3. Salary range
    4. Industry trends
    Format the response in markdown with clear headings and bullet points.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit App
def main():
    st.title("🔍 Job Search Assistant")

    job_title = st.text_input("Enter job title or keywords:")
    location = st.text_input("Location:")

    if st.button("Search Jobs"):
        linkedin_url, naukri_url = search_jobs(job_title, location)
        st.markdown(f"[View Jobs on LinkedIn]({linkedin_url})")
        st.markdown(f"[View Jobs on Naukri]({naukri_url})")

        with st.spinner("Fetching job search tips..."):
            tips = get_job_search_tips(job_title)
            st.markdown(tips)

if __name__ == "__main__":
    main()
