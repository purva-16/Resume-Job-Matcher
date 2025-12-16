## Resume–Job Description Matcher

### What it does
This project is an explainable NLP-based system that evaluates how well a resume matches a given job description. Instead of relying only on keyword matching, it uses semantic text representations to understand contextual similarity and provides clear insights into matched and missing skills.

### How it works
The system extracts text from uploaded resume and job description files and performs linguistic preprocessing using spaCy. Contextual embeddings are generated using Sentence-BERT, and cosine similarity is used to compute an overall match score. A controlled skill vocabulary is applied to identify overlapping and missing skills, making the results interpretable and actionable.

### Inputs
- Resume file (PDF)
- Job description file (PDF or TXT)

### Output
- Match percentage based on semantic similarity  
- List of matched skills  
- List of missing or weak skills  
