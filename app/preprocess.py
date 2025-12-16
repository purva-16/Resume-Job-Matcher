import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return " ".join(page.extract_text() or "" for page in pdf.pages)
    return file.file.read().decode("utf-8")

def clean_text(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return " ".join(tokens)
