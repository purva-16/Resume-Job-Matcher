from fastapi import FastAPI, UploadFile, File
from app.preprocess import extract_text, clean_text
from app.skills import extract_skills
from app.similarity import get_similarity
from app.explain import explain

app = FastAPI(title="Resume–JD Matcher API")

@app.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    resume_text = clean_text(extract_text(resume))
    jd_text = clean_text(extract_text(job_description))

    similarity_score = get_similarity(resume_text, jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    explanation = explain(resume_skills, jd_skills)

    return {
        "match_percentage": round(similarity_score * 100, 2),
        "matched_skills": explanation["matched_skills"],
        "missing_skills": explanation["missing_skills"]
    }
