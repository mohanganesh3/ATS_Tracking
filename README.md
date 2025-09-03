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

## Deployment to Vercel

This application is configured for deployment to Vercel with the following settings:

### Build Command
```
pip install -r requirements.txt
```

### Start Command
```
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

### Environment Variables
Set the following environment variable in your Vercel project settings:
- `GOOGLE_API_KEY`: Your Google Gemini API key

### Configuration
The `.streamlit/config.toml` file is configured to:
- Use polling instead of file watchers to avoid inotify limits
- Set appropriate server settings for Vercel deployment

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
- For Vercel deployment, file watching is disabled to prevent inotify limits