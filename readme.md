AI Resume Reviewer

AI-powered resume analysis tool that reviews resumes, identifies strengths and weaknesses, evaluates ATS compatibility, and provides actionable improvement suggestions.

Live Backend:

https://ai-resume-reviewer-1.onrender.com

Features:

* Upload PDF resumes
* AI-powered resume analysis using Gemini
* Resume scoring
* ATS compatibility review
* Strengths and weaknesses analysis
* Technical skills evaluation
* Project evaluation
* Interview readiness assessment
* Actionable improvement suggestions

Screenshots:

Home Page

![homepage](screenshots/homepage.png)

Analysis Result

![results](screenshots/result.png)

Tech Stack:

Backend

* Python
* Flask
* Flask-CORS
* Google Gemini API
* PyMuPDF
* Gunicorn

Frontend

* HTML
* CSS
* JavaScript

Deployment

* Render
* GitHub

Project Structure:

ai-resume-reviewer/
│
├── backend.py
├── frontend.html
├── requirements.txt
├── Procfile
├── README.md
├── screenshots/
│   ├── homepage.png
│   └── result.png

API Endpoint

Analyze Resume

POST /review

Upload a PDF resume and receive AI-generated feedback.

Edge Cases Handled

* No file uploaded
* Invalid PDF file
* Empty PDF
* PDF exceeds 5 pages
* AI service unavailable
* Unsupported file type

What I Learned

* Flask API development
* File uploads in Flask
* PDF processing with PyMuPDF
* Gemini API integration
* Error handling
* Environment variables
* Git and GitHub workflows
* Deployment using Render
* Frontend to backend communication

Future Improvements

* Structured JSON responses
* Better frontend formatting
* Resume history
* Downloadable reports
* Authentication system
* Full frontend deployment

Author

Sabir Ahmed