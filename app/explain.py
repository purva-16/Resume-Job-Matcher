def explain(resume_skills: set, jd_skills: set) -> dict:
    return {
        "matched_skills": list(resume_skills & jd_skills),
        "missing_skills": list(jd_skills - resume_skills)
    }
