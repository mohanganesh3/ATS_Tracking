import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        text += str(page_content.extract_text())
    return text

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
    if uploaded_file is not None:
        try:
            text = input_pdf_text(uploaded_file)
            formatted_prompt = input_prompt.format(text=text, jd=jd)
            response = get_gemini_response(formatted_prompt)
            
            # Try to parse the response as JSON
            try:
                response_data = json.loads(response)
                st.subheader("ATS Analysis Result")
                
                # Display JD Match
                st.write("**Job Description Match:** ", response_data["JD Match"])
                
                # Display Missing Keywords
                st.write("**Missing Keywords:**")
                for keyword in response_data["MissingKeywords"]:
                    st.write(f"- {keyword}")
                
                # Display Profile Summary
                st.write("**Profile Summary:**")
                st.write(response_data["Profile Summary"])
                
            except json.JSONDecodeError:
                # If JSON parsing fails, display the raw response
                st.subheader("Response")
                st.write(response)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please upload a resume file")