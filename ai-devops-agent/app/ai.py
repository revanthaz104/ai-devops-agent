import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def analyze_log_with_ai(log: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a senior DevOps + SRE engineer.

Analyze logs and provide:
1. Root cause
2. Fix
3. Prevention
"""
                },
                {
                    "role": "user",
                    "content": log
                }
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"AI unavailable, fallback triggered. Error: {str(e)}"


# Fallback logic (important for demo reliability)
def fallback_analysis(log: str):
    log = log.lower()

    if "timeout" in log:
        return "Timeout issue detected. Increase timeout or optimize pipeline steps."

    elif "docker" in log:
        return "Docker build failure. Check Dockerfile and build context."

    elif "memory" in log:
        return "Memory issue. Increase resources or optimize usage."

    return "General pipeline failure. Check logs and retry."