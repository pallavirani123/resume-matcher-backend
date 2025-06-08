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
    resume_tokens = tokenize(resume_text)
    job_tokens = tokenize(job_description)

    matched_keywords = list(set(resume_tokens).intersection(job_tokens))
    missing_keywords = list(set(job_tokens) - set(resume_tokens))

    score = round(len(matched_keywords) / len(job_tokens) * 100, 1) if job_tokens else 0

    feedback = (
        "Try adding these keywords: " + ", ".join(missing_keywords[:5])
        if missing_keywords else "Great match!"
    )

    return score, matched_keywords, feedback
