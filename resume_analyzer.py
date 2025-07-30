import streamlit as st
import os
import json
import pdfplumber
import docx
import google.generativeai as genai



def setup_gemini(api_key: str):
    """
    Configure the Gemini Flash API with your API key and return the model instance.
    """
    #place your own_api_key
    genai.configure(api_key="AIzaSyDJQC1tWpupjjAhc6d7CqkA8u1j3V3WTKg")
    return genai.GenerativeModel("gemini-2.0-flash")

def extract_text_from_pdf(file) -> str:
    """
    Extract all text from a PDF file.
    """
    with pdfplumber.open(file) as pdf:
        text = "\n".join(page.extract_text() or '' for page in pdf.pages)
    return text.strip()

def extract_text_from_docx(file) -> str:
    """
    Extract all text from a DOCX file.
    """
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs]).strip()

def generate_summary(model, resume_text: str) -> str:
    """
    Use Gemini Flash to generate a short summary of the resume.
    """
    prompt = f"Summarize this resume in 5-6 lines:\n\n{resume_text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def check_job_match(model, summary: str, job_description: str) -> str:
    """
    Use Gemini Flash to compare resume summary and job description, returning a match score and decision.
    """
    prompt = f"""
    Compare the following resume summary and job description. 
    Return a score out of 100 and whether it's a match or not.

    Resume Summary:
    {summary}

    Job Description:
    {job_description}
    """
    response = model.generate_content(prompt)
    return response.text.strip()


def main():
    st.set_page_config(page_title="AI Resume Screening Tool", layout="centered")
    st.title("📄 AI Resume Screening Tool")
    st.write("Upload a resume and enter a job description to check for a match.")

    # User input: Job description text area
    job_description = st.text_area(
        label="Enter Job Description",
        height=150,
        placeholder="Paste the job description here..."
    )

    # File uploader: accepts PDF or DOCX
    uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

    # Gemini API key input (or hardcode here)
    GEMINI_API_KEY = st.text_input("Enter Gemini API Key", type="password")

    if uploaded_file and job_description.strip() and GEMINI_API_KEY.strip():

        if st.button("Analyze Resume"):

            with st.spinner("Processing..."):

                # Extract resume text depending on file type
                if uploaded_file.name.endswith(".pdf"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                else:
                    resume_text = extract_text_from_docx(uploaded_file)

                # Setup Gemini model
                model = setup_gemini(GEMINI_API_KEY)

                # Generate summary from resume text
                summary = generate_summary(model, resume_text)

                # Check match between summary and user-given job description
                match_result = check_job_match(model, summary, job_description)

                # Show results on app
                st.subheader("📌 Resume Summary")
                st.success(summary)

                st.subheader("🎯 Job Match Result")
                st.info(match_result)

                # Save output locally as JSON
                output = {
                    "resume_summary": summary,
                    "job_description": job_description,
                    "match_result": match_result
                }
                os.makedirs("outputs", exist_ok=True)
                output_path = os.path.join("outputs", "summary.json")
                with open(output_path, "w") as f:
                    json.dump(output, f, indent=2)

                st.success(f"✅ Results saved to `{output_path}`")

    else:
        st.info("Please upload a resume, enter the job description, and provide your Gemini API key.")

if __name__ == "__main__":
    main()
