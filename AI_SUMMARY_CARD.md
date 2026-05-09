# AI SUMMARY CARD

# Project Name
Tool-32 — Procedure Documentation Tool

---

# What This Project Does

This project uses AI to:

- Generate descriptions
- Give recommendations
- Generate reports

---

# AI Technology Used

- Python 3.11
- Flask
- Groq API
- LLaMA 3.3 70B
- Redis
- Docker
- Spring Boot

---

# AI Endpoints

## 1. POST /describe

Purpose:
Generate AI summary.

Example:

```json
{
  "summary": "Server backup failed.",
  "priority": "High"
}
```

---

## 2. POST /recommend

Purpose:
Generate recommendations.

Example:

```json
[
  {
    "description": "Check database indexes."
  }
]
```

---

## 3. POST /generate-report

Purpose:
Generate AI report.

Example:

```json
{
  "title": "Security Report",
  "summary": "Multiple login failures detected."
}
```

---

# Security Features

- JWT Authentication
- Prompt Injection Protection
- SQL Injection Protection
- Rate Limiting
- XSS Sanitization

---

# AI Workflow

```text
Frontend
   ↓
Spring Boot Backend
   ↓
Flask AI Service
   ↓
Groq AI Model
   ↓
AI Response
```

---

# Health Endpoint

```text
http://localhost:5000/health
```

Example:

```json
{
  "status": "UP"
}
```

---

# GitHub Repository

Add your GitHub link here.

---

# Demo Talking Points

- AI creates summaries automatically
- AI gives recommendations
- AI generates reports
- Flask handles AI requests
- Groq provides AI model

---

# Final Status

 AI Service Working  
 Security Completed  
 Docker Tested  
 Demo Ready