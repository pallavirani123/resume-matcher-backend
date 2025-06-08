from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.parser import parse_resume
from utils.keywords import extract_keywords, match_keywords, score_resume

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    resume = request.files.get("resume")
    job_desc = request.form.get("job_description", "")

    if not resume:
        return jsonify({"error": "Resume file is missing"}), 400

    path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(path)

    resume_text = parse_resume(path)
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)
    match_result = match_keywords(resume_keywords, job_keywords)

    score, matched_keywords, feedback = score_resume(resume_text, job_desc)

    return jsonify({
        "score": score,
        "matched_keywords": matched_keywords,
        "feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)
