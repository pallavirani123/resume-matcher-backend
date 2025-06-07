import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def tokenize(text):
    tokens = re.findall(r"\b\w{3,}\b", text.lower())
    return [t for t in tokens if t not in ENGLISH_STOP_WORDS]

def extract_keywords(text, top_n=20):
    tokens = tokenize(text)
    freq = Counter(tokens)
    return [word for word, _ in freq.most_common(top_n)]

def match_keywords(resume_keywords, job_keywords):
    matched = [k for k in job_keywords if k in resume_keywords]
    missing = [k for k in job_keywords if k not in resume_keywords]
    score = len(matched) / len(job_keywords) * 100 if job_keywords else 0
    return {"score": round(score, 1), "matched": matched, "missing": missing}
def score_resume(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    matched_keywords = resume_words.intersection(job_words)
    score = len(matched_keywords)

    missing_keywords = job_words - resume_words
    feedback = "Try adding these keywords: " + ", ".join(list(missing_keywords)[:5]) if missing_keywords else "Great match!"

    return score, list(matched_keywords), feedback
