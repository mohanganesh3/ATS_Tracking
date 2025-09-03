# Smart ATS - Resume Optimizer

Smart ATS is a web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). It provides actionable insights by analyzing resumes against job descriptions using AI.

## Features

- Resume upload (PDF format)
- Job description input
- Resume analysis and match percentage
- Missing keywords identification
- Personalized profile summary

## Technology Stack

- **Frontend/Backend**: Streamlit (Python)
- **AI Analysis**: Google Gemini AI
- **PDF Processing**: PyPDF2
- **Environment Management**: python-dotenv

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smart-ats
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Google Gemini API key:
   ```env
   GOOGLE_API_KEY=your_actual_google_api_key_here
   ```
   You can get your API key from: https://makersuite.google.com/app/apikey

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Deployment to Streamlit Community Cloud

This application is configured for deployment to Streamlit Community Cloud with the following settings:

### Deployment Steps
1. Visit [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in with your GitHub account
2. Click on "New app"
3. Select your repository (mohanganesh3/ATS_Tracking)
4. Set the branch to "main"
5. Set the main file path to "app.py"
6. Click "Deploy"

### Environment Variables
In the Streamlit Cloud settings, you must add your Google API key:
- Key: `GOOGLE_API_KEY`
- Value: Your actual Google Gemini API key (get it from https://makersuite.google.com/app/apikey)

### Configuration
The application includes configuration to:
- Avoid file watcher issues that cause deployment problems
- Handle API authentication errors gracefully
- Provide clear error messages to users

## Directory Structure
```
smart-ats/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not committed)
├── .streamlit/
│   └── config.toml    # Streamlit configuration
└── README.md          # This file
```

## Usage

1. Visit the application in your browser
2. Paste a job description in the text area
3. Upload your resume in PDF format
4. Click "Submit" to get AI-powered analysis
5. Review the match percentage, missing keywords, and profile summary

## Notes

- Only PDF resumes are supported
- The application requires a Google Gemini API key for AI analysis
- File watching is minimized to avoid issues on cloud platforms
- Error handling is implemented for common issues like missing API keys or PDF parsing errors