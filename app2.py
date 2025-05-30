import streamlit as st
import google.generativeai as genai
from docx import Document
import PyPDF2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
def initialize_model():
    return genai.GenerativeModel('gemini-1.5-flash')

# Function to extract text from resume
def extract_text_from_resume(file):
    text = ""
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

# Function to analyze resume and generate score
def analyze_resume(file):
    resume_text = extract_text_from_resume(file)
    
    if not resume_text.strip():
        return "Error: Could not extract text from the resume. Please upload a valid file."

    prompt = f"""
    Analyze the following resume based on these key aspects:
    1. **Skills & Experience** (Relevance to the industry)
    2. **Formatting & Structure** (Proper headings, sections, readability)
    3. **Grammar & Clarity** (Professional and error-free language)
    4. **Industry Relevance** (Does it match job expectations?)
    
    Provide:
    - A **score out of 100** based on these factors.
    - Key strengths and areas for improvement.
    - Suggestions for enhancing the resume.

    Resume Content:
    {resume_text}
    """

    model = initialize_model()
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
def main():
    st.title("📄 Resume Analyzer")
    
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_file and st.button("Analyze Resume"):
        with st.spinner("Analyzing your resume..."):
            analysis = analyze_resume(uploaded_file)
            st.markdown(analysis)

if __name__ == "__main__":
    main()
