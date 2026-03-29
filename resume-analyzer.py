import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Resume and Job Description
# -----------------------------
resume = """
Python developer skilled in machine learning, pandas, and data analysis.
"""

job_desc = """
Looking for a Python developer with knowledge of machine learning, pandas, numpy, and scikit-learn.
"""

# -----------------------------
# Clean text
# -----------------------------
def clean(text):
    text = text.lower()
    text = text.replace("scikit-learn", "scikitlearn")  # keep as one word
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # remove punctuation
    return text

resume_clean = clean(resume)
job_clean = clean(job_desc)

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform([resume_clean, job_clean])

# -----------------------------
# Similarity Score
# -----------------------------
similarity = cosine_similarity(vectors[0:1], vectors[1:2])
score = similarity[0][0] * 100

print("\nMatch Score:", round(score, 2), "%")

# -----------------------------
# Stopwords Removal for Keywords
# -----------------------------
stopwords = set([
    "the", "is", "in", "and", "to", "of", "for", "with", "a", "an", "on",
    "looking", "knowledge", "developer"
])

resume_words = set(resume_clean.split()) - stopwords
job_words = set(job_clean.split()) - stopwords

# -----------------------------
# Missing Keywords
# -----------------------------
missing = job_words - resume_words

print("\nMissing Keywords:")
for word in missing:
    print("-", word)
