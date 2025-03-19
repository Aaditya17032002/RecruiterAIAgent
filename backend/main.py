from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import re
from langchain_groq import ChatGroq
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Models ---
class JobDescription(BaseModel):
    description: str

class CandidateResult(BaseModel):
    resume_number: int
    candidate_name: str
    candidate_details: str
    matching_skills: str
    bias_mitigated_details: str
    score: float

# --- Helper Functions ---
def strip_markdown(text: str) -> str:
    text = re.sub(r'[`*_~]', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    return text

def extract_numeric_score(score_str: str) -> float:
    match = re.search(r'\d+(\.\d+)?', score_str)
    if match:
        return float(match.group())
    return 0.0

def extract_candidate_name(resume: str) -> str:
    for line in resume.splitlines():
        line = line.strip()
        if line:
            return line
    return "Unknown"

# --- API Keys and LLM Setup ---
userdata = {
    'groq_api_key': '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',
    'LANGSMITH_API_KEY': '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'
}

groq_api_key = userdata.get('groq_api_key')
langsmith = userdata.get('LANGSMITH_API_KEY')

os.environ["LANGCHAIN_API_KEY"] = langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"

llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

def call_llama(prompt: str) -> str:
    messages = [{"role": "user", "content": prompt}]
    response = llm.invoke(messages, max_tokens=5500, temperature=0.5)
    return strip_markdown(response.content.strip())

# --- Node Classes ---
class JobPostingNode:
    @staticmethod
    def process(job_description: str) -> dict:
        prompt = (
            "Extract key requirements, skills, and qualifications from the following job description:\n\n"
            f"{job_description}"
        )
        llm_response = call_llama(prompt)
        return {"job_analysis": llm_response}

class ResumeParserNode:
    @staticmethod
    def process(resume: str) -> dict:
        prompt = """
        As an expert recruiter, analyze this resume and provide a structured output in the following format:
        {
            "personal_info": {
                "name": "",
                "contact": "",
                "location": "",
                "summary": ""
            },
            "skills": {
                "technical": [],
                "soft": [],
                "tools": []
            },
            "experience": [
                {
                    "title": "",
                    "company": "",
                    "duration": "",
                    "highlights": []
                }
            ],
            "education": [
                {
                    "degree": "",
                    "institution": "",
                    "year": "",
                    "field": ""
                }
            ],
            "certifications": [],
            "achievements": []
        }

        Extract and categorize all information from this resume:

        {resume}
        """
        llm_response = call_llama(prompt.format(resume=resume))
        try:
            # Parse the response as JSON
            parsed_data = json.loads(llm_response)
            return {"parsed_resume": parsed_data}
        except:
            return {"parsed_resume": llm_response}

class SkillMatcherNode:
    @staticmethod
    def process(candidate_details: str, job_requirements: str) -> dict:
        prompt = """
        As a senior technical recruiter, analyze the candidate's skills against the job requirements.
        Provide a structured analysis in the following format:
        {
            "matching_skills": {
                "technical": {
                    "matched": [],
                    "partially_matched": [],
                    "missing": []
                },
                "soft_skills": {
                    "matched": [],
                    "missing": []
                },
                "tools_and_technologies": {
                    "matched": [],
                    "similar": [],
                    "missing": []
                }
            },
            "experience_match": {
                "years": "X years",
                "relevance": "High/Medium/Low",
                "key_highlights": []
            },
            "overall_analysis": ""
        }

        Candidate Details: {candidate_details}
        Job Requirements: {job_requirements}
        """
        llm_response = call_llama(prompt.format(
            candidate_details=candidate_details,
            job_requirements=job_requirements
        ))
        try:
            return {"matching_skills": json.loads(llm_response)}
        except:
            return {"matching_skills": llm_response}

class BiasMitigatorNode:
    @staticmethod
    def process(candidate_details: str) -> dict:
        prompt = (
            "Rewrite the following candidate details to remove any potentially biased language while preserving all critical technical and professional details. "
            "Act as a recruiter with 25+ years of experience who is extremely meticulous and unbiased.\n\n"
            f"{candidate_details}"
        )
        llm_response = call_llama(prompt)
        return {"bias_mitigated_details": llm_response}

class ScoringNode:
    @staticmethod
    def process(candidate_details: str, matching_skills: str) -> dict:
        prompt = (
            "You are a highly experienced recruiter with over 25 years in technology and recruitment. "
            "Examine the candidate details and the matching skills in minute detail. "
            "Score the candidate's overall fit for the role as a percentage from 0% to 100%. "
            "Return only the percentage value (e.g., '85%').\n\n"
            f"Candidate Details: {candidate_details}\n\nMatching Skills: {matching_skills}"
        )
        llm_response = call_llama(prompt)
        return {"score": llm_response}

# --- API Endpoints ---
@app.post("/api/job-description")
async def analyze_job_description(job: JobDescription):
    try:
        job_posting_node = JobPostingNode()
        job_analysis = job_posting_node.process(job.description)
        return {"job_requirements": job_analysis.get("job_analysis", "")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/extract-resume-info")
async def extract_resume_info(
    resume_text: str = Form(...),
    job_description: Optional[str] = Form(None)
):
    print(f"Received job description: {job_description}")
    print(f"Received resume text: {resume_text}")

    # Your processing logic here
    # For example, you can parse the resume text and analyze it based on the job description

    return {"message": "Resume processed successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 