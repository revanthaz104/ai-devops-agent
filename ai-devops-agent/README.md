# 🚀 AI DevOps Agent

This is a simple AI-powered DevOps assistant that analyzes CI/CD pipeline logs and suggests possible fixes.

## 🔧 Features

- Analyze pipeline logs
- Identify root cause
- Suggest fixes and prevention
- Fallback logic when AI is unavailable

## 🛠️ Tech Stack

- FastAPI
- OpenAI API
- Pydantic

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload