# ats_scoring.py
# AI Resume Scoring & Improvements

import spacy
from Job_matcher import JobMatcher
from collections import Counter
class ATSScoring:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.job_matcher = JobMatcher()

    def score_resume(self, resume_file, job_description):
        """Scores the resume based on ATS keywords match"""
        # Pass the actual file to resume_parser
        resume_data = self.job_matcher.resume_parser.parse_resume(resume_file)
        
        # Extract text from the parsed resume
        resume_text = resume_data["text"]
        
        # Continue with job description processing
        job_doc = self.nlp(job_description)
        resume_doc = self.nlp(resume_text)
        
        job_keywords = [token.text.lower() for token in job_doc if token.is_alpha]
        resume_keywords = [token.text.lower() for token in resume_doc if token.is_alpha]
        
        match_score = sum((Counter(resume_keywords) & Counter(job_keywords)).values())
        total_keywords = len(set(job_keywords))
        match_percentage = (match_score / total_keywords) * 100 if total_keywords > 0 else 0

        return {
            "ats_score": match_percentage,
            "matched_keywords": list(set(resume_keywords) & set(job_keywords))
        }

if __name__ == "__main__":
    ats = ATSScoring()
    sample_resume = "sample_resume.pdf"  # Change to actual file path
    sample_job_desc = "Looking for a Python Developer with experience in Machine Learning and SQL."
    result = ats.score_resume(sample_resume, sample_job_desc)
    print(result)
