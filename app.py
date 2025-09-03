import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating response from Gemini: {str(e)}")
        return None

def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page_content = reader.pages[page]
            text += str(page_content.extract_text())
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {str(e)}")
        return None

#Prompt Template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy.

resume: {text}
description: {jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if not api_key:
        st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable in Streamlit Cloud settings.")
    elif uploaded_file is not None:
        try:
            text = input_pdf_text(uploaded_file)
            if text is not None:
                formatted_prompt = input_prompt.format(text=text, jd=jd)
                response = get_gemini_response(formatted_prompt)
                
                if response:
                    # Try to parse the response as JSON
                    try:
                        response_data = json.loads(response)
                        st.subheader("ATS Analysis Result")
                        
                        # Display JD Match
                        st.write("**Job Description Match:** ", response_data.get("JD Match", "N/A"))
                        
                        # Display Missing Keywords
                        st.write("**Missing Keywords:**")
                        missing_keywords = response_data.get("MissingKeywords", [])
                        if missing_keywords:
                            for keyword in missing_keywords:
                                st.write(f"- {keyword}")
                        else:
                            st.write("No missing keywords found.")
                        
                        # Display Profile Summary
                        st.write("**Profile Summary:**")
                        st.write(response_data.get("Profile Summary", "N/A"))
                        
                    except json.JSONDecodeError:
                        # If JSON parsing fails, display the raw response
                        st.subheader("Response")
                        st.write(response)
            else:
                st.error("Failed to extract text from the PDF file.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please upload a resume file")