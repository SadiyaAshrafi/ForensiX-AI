from fastapi import FastAPI


app = FastAPI(
    title="ForensiX AI",
    description="AI-Assisted Cyber Forensic Triage Platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "ForensiX AI",
        "message": "Cyber Forensic Triage Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }