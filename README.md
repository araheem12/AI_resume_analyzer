AI Resume Screening Tool
Project Overview
This project implements an AI-driven Resume Screening Tool built with Python and Streamlit. It automates the process of analyzing candidate resumes by summarizing resume content using the Gemini Flash model and comparing the summary against a provided job description to determine suitability.
Features
•	Upload resumes in PDF or DOCX formats.
•	Extract text content from uploaded resumes.
•	Generate a concise summary of the resume using Google’s Gemini Flash language model.
•	Allow user input for job descriptions to customize the screening.
•	Compare the resume summary with the job description to compute a match score and provide a match/no-match result.
•	Save the summary and match result as a JSON output file.
•	User-friendly web interface built with Streamlit.
Tech Stack
•	Python 3.8+
•	Streamlit for interactive UI
•	pdfplumber for PDF text extraction
•	python-docx for DOCX text extraction
•	Google Generative AI Gemini Flash model (`google-generativeai` Python SDK)
Setup and Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-resume-screening-tool.git
   cd ai-resume-screening-tool
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your Gemini API key as an environment variable:

   - Windows PowerShell:

     ```powershell
     $env:GOOGLE_API_KEY="your_api_key_here"
     ```

   - macOS/Linux:

     ```bash
     export GOOGLE_API_KEY="your_api_key_here"
     ```

Usage
Run the Streamlit app with:

```bash
python -m streamlit run resume_analyzer.py
```

- Open the provided URL in your browser.
- Paste the job description into the text box.
- Upload a resume file (PDF or DOCX).
- Enter your Gemini API key.
- Click “Analyze Resume” to view the summary and match result.
- Results are saved in the `outputs/summary.json` file.

Project Structure
ai-resume-screening-tool/
├── resume_analyzer.py       # Main Streamlit app and logic
├── requirements.txt         # Project dependencies
├── outputs/                 # Folder where JSON output is saved
└── README.docx              # This README document

Notes
- Ensure that your Gemini API key is valid and has permissions to access the Gemini Flash model.
- This project can be extended to include email/WhatsApp alerts or consent workflows.
- Error handling and logging can be added for production readiness.

License
MIT License © 2025 Abdul Raheem
Contact
For questions or collaboration, contact Abdul Raheem at [your_email@example.com].
