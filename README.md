# Here’s a creative and engaging README file for your project:

## 📄 Smart ATS

Enhance Your Resume to Ace the Job Market!

Smart ATS is a web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). Powered by Google Gemini and Streamlit, it evaluates resumes against a job description, identifies missing keywords, and provides actionable feedback to boost your chances of landing the perfect job.
## 🎬 Demo

<img width="639" alt="Screenshot 2024-12-13 at 6 40 20 AM" src="https://github.com/user-attachments/assets/c69d396b-a60d-4514-981c-564c93bfdfea" />

1.Paste Job Description: Enter the JD in the text area.
2.Upload Resume: Click “Upload Your Resume” and select a PDF file.
<img width="632" alt="Screenshot 2024-12-13 at 6 43 37 AM" src="https://github.com/user-attachments/assets/c5193bd3-ff7a-4ac5-ba87-600dfdf03020" />

3.Get Insights: Hit “Submit” and view your results instantly!
<img width="635" alt="Screenshot 2024-12-13 at 6 43 56 AM" src="https://github.com/user-attachments/assets/3558c606-f75e-4574-8514-c2aa224d0c7a" />

## 🚀 Features
	•	📋 Resume Analysis: Upload your resume as a PDF, and let Smart ATS evaluate it.
	•	🔍 JD Matching: Get a percentage match with the job description.
	•	📝 Keyword Insights: Discover missing keywords essential for the role.
	•	🌟 Profile Summary: Receive a personalized profile summary tailored to the job description.

## 🛠️ Technologies Used
	•	Streamlit: For building the user-friendly interface.
	•	Google Gemini AI: To analyze and generate high-quality insights.
	•	PyPDF2: For extracting text from PDF resumes.
	•	dotenv: For securely managing API keys.

## 📖 How It Works
	1.	Paste the Job Description in the provided text area.
	2.	Upload your Resume in PDF format.
	3.	Click Submit, and let the app do its magic!
	4.	View your resume’s JD match percentage, missing keywords, and profile summary.

## 🖥️ Step by Step 

Step 1: Clone the Repository

git clone https://github.com/your-username/smart-ats.git
cd smart-ats

Step 2: Set Up the Environment

Create a virtual environment (optional but recommended) and install dependencies:

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install streamlit google-generativeai PyPDF2 python-dotenv

Step 3: Configure API Key
	•	Obtain your Google Gemini API Key.
	•	Create a .env file in the project directory with the following content:

GOOGLE_API_KEY=your_google_api_key



Step 4: Run the Application

Start the Streamlit app:

streamlit run app.py

Step 5: Use the App
	•	Paste Job Description: Enter the JD in the text area.
	•	Upload Resume: Click “Upload Your Resume” and select a PDF file.
	•	Get Insights: Hit “Submit” and view your results instantly!

## 📂 Project Structure

smart-ats/
├── app.py                # Main application code
├── .env                  # API keys (add this manually)
├── requirements.txt      # Python dependencies

## 🌟 Example Output

Input:
	•	Job Description: “Data Scientist with expertise in Python, ML, and NLP.”
	•	Resume: PDF file with details of experience and skills.

Output:

{
  "JD Match": "85%",
  "MissingKeywords": ["NLP", "Big Data"],
  "Profile Summary": "Experienced Data Scientist skilled in Python and ML. Adding expertise in NLP will enhance your profile for this role."
}

## 🛡️ Future Enhancements
	•	🌐 Support for multiple resume formats (e.g., Word).
	•	📊 Visualizations for JD match percentage and keyword density.
	•	🤖 Integration with LinkedIn for automatic profile suggestions.

## 🤝 Contributing

We welcome contributions! Feel free to submit issues or pull requests to enhance the app.

## 🧑‍💻 Author

Mohan Ganesh Gottipati
2nd-year CSE student at IIIT Sri City
GitHub | Email
