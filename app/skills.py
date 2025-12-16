SKILL_SET = {
    "python", "nlp", "machine learning", "deep learning",
    "sql", "pandas", "numpy", "scikit-learn",
    "tensorflow", "docker", "aws", "api", "fastapi"
}

def extract_skills(text: str) -> set:
    return {skill for skill in SKILL_SET if skill in text}
