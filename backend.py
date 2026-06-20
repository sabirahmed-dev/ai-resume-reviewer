import os 
from flask_cors import CORS
from google import genai
import fitz
from flask import Flask,request

app = Flask(__name__)
CORS(app)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = """
    You are an expert technical recruiter, hiring manager, and resume reviewer with experience evaluating resumes for internships, entry-level software engineering roles, full-stack development roles, backend development roles, AI application development roles, and GenAI-related positions.

    Your task is to analyze the provided resume objectively and provide actionable feedback.

    Evaluate the resume based on:

    * Resume structure and formatting
    * Technical skills
    * Projects
    * Education
    * Work experience (if present)
    * Achievements
    * Clarity and readability
    * ATS (Applicant Tracking System) friendliness
    * Relevance to modern software engineering and AI industry expectations
    * Overall professionalism

    Return your response in the following exact format:

    RESUME_SCORE:
    <score out of 100>

    SUMMARY:
    STRENGTHS:

    * <strength 1>
    * <strength 2>
    * <strength 3>
    * <strength 4>
    * <strength 5>

    WEAKNESSES:

    * <weakness 1>
    * <weakness 2>
    * <weakness 3>
    * <weakness 4>
    * <weakness 5>

    MISSING_ELEMENTS:

    * <missing item 1>
    * <missing item 2>
    * <missing item 3>

    ATS_ANALYSIS:
    PROJECT_ANALYSIS:
    TECHNICAL_SKILLS_ANALYSIS:
    INTERVIEW_READINESS:
    TOP_PRIORITY_IMPROVEMENTS:

    <highest priority improvement>
    <second highest priority improvement>
    <third highest priority improvement>

    DETAILED_SUGGESTIONS:

    * <actionable suggestion 1>
    * <actionable suggestion 2>
    * <actionable suggestion 3>
    * <actionable suggestion 4>
    * <actionable suggestion 5>

    FINAL_VERDICT:
    Rules:

    * Be honest and critical.
    * Do not inflate scores.
    * Explain reasoning clearly.
    * Focus on practical improvements.
    * Avoid generic motivational statements.
    * Assume the candidate wants to maximize internship opportunities in software engineering and AI-related roles.
    * If information is missing, explicitly mention it.
    * Base all feedback only on the provided resume.

    keep all thing short and simple and more structured

    Resume Content:

    """


@app.route("/")
def get_resume():
    return "Resume Reviewer API"


@app.route("/review",methods=["POST"])
def post_resume():

    if "pdf" not in request.files:
        return "NO file uploded"


    pdf = request.files["pdf"]

    if not pdf.filename.lower().endswith(".pdf"):
        return "Only pdf files allowed"
    
    pdf.save("sample.pdf")

    try:
        doc = fitz.open("sample.pdf")
    except:
        return "Invalid or Courrupted pdf"

    text = ""
    
    if len(doc) > 5:
        return "You cant exceed more then 5 pages in pdf"
    
    for page in doc:
        text += page.get_text()

    if not text.strip():
        return "The pdf is empty"

    full_prompt = prompt + text

    models = [
        "gemini-3.5-flash",
        "gemini-2.5-flash",
        "gemini-2.5-pro"
        ]

    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=full_prompt
            )
            return response.text
        except Exception:
            continue

    return "All Gemini models are currently unavailable. Please try again later."

if __name__ == "__main__":
    app.run(debug=True)


    
    
