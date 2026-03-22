from fastapi import FastAPI
from app.models import LogInput
from app.ai import analyze_log_with_ai, fallback_analysis

app = FastAPI(title="AI DevOps Agent")

@app.get("/")
def home():
    return {"message": "AI DevOps Agent Running 🚀"}


@app.post("/analyze")
def analyze(input: LogInput):
    # Try AI first
    result = analyze_log_with_ai(input.log)

    # If AI fails, fallback
    if "AI unavailable" in result:
        result = fallback_analysis(input.log)

    return {
        "input_log": input.log,
        "analysis": result
    }