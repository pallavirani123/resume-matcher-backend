# 🔍 AI-Powered Resume Matcher – Backend

This is the backend of the **AI Resume Matcher**, a web-based tool that helps job seekers evaluate how well their resume aligns with a given job description. The backend is powered by Flask and uses Natural Language Processing (NLP) techniques to extract keywords, compute similarity scores, and generate actionable feedback.

---

## 🚀 Features

- Upload resumes in PDF, DOCX, or TXT format
- Extract and compare keywords between resume and job description
- Generate a **match score**, list of **matched keywords**, and **improvement suggestions**
- Designed for integration with a frontend (hosted on GitHub Pages)
- Built-in support for CORS, enabling cross-origin requests

---

## 🧠 Tech Stack

- **Python 3.11**
- **Flask** – Lightweight web framework
- **pdfminer.six** – PDF parsing
- **python-docx** – DOCX parsing
- **scikit-learn** – Stopword filtering
- **Flask-CORS** – Cross-origin support
- **Render** – Backend deployment

---

## 📁 Folder Structure
resume-matcher-backend/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── README.md # Project overview and documentation
├── pallaviResume1.pdf # Sample resume file for testing
├── utils/
│ ├── pycache/ # Python bytecode cache
│ ├── keywords.py # Logic for keyword extraction and scoring
│ └── parser.py # Resume file parsing (PDF, DOCX, TXT)
└── .gitignore # Ignore unnecessary files


---

## 🔄 Application Flow

1. The **frontend** sends a POST request to the `/upload` API with:
   - Resume file
   - Job description text

2. Flask handles the file upload and saves it temporarily.

3. The backend extracts text from the resume using:
   - `pdfminer.six` for PDFs
   - `python-docx` for Word documents
   - Native reading for TXT files

4. Both the resume and job description are tokenized and cleaned to extract meaningful keywords.

5. A **match score** is calculated based on keyword overlap.

6. The response includes:
   - Match score (percentage)
   - List of matched keywords
   - Feedback suggesting missing keywords to improve the resume

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pallavirani123/resume-matcher-backend.git
cd resume-matcher-backend
### 2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3.Install Dependencies

pip install -r requirements.txt

### 4. Run the App

python app.py

The API will be accessible at: http://127.0.0.1:5000/upload

🌐 API Endpoint
POST /upload

form-data:

resume: Resume file (PDF, DOCX, or TXT)

job_description: Plain text job description

Response:

{
  "score": 82.1,
  "matched_keywords": ["python", "aws", "nlp", ...],
  "feedback": "Try adding these keywords: docker, ci/cd, scalable, restful"
}
📦 Deployment
The backend is deployed on Render and accessible through the following API base URL:

https://resume-matcher-api-rkvj.onrender.com

You can integrate it with the frontend via this URL in your JavaScript.

📌 Frontend Repository
The frontend is hosted separately on GitHub Pages and can be found here:

👉 https://github.com/pallavirani123/resume-matcher-frontend

🙋‍♀️ About the Developer

Pallavi Rani Velagala
Passionate about building impactful data and AI-driven applications.

Connect with me on LinkedIn

https://www.linkedin.com/in/pallavirani-velagala-41434625b/
