# AI DEMO SCRIPT

## 1. Introduction

Say:

"This project uses AI to generate descriptions, recommendations, and reports automatically."

---

# 2. AI Describe Demo

## Input

```text
Server backup failed during maintenance.
```

## What To Do
- Create new record
- Click AI Describe

## Expected Output

```json
{
  "summary": "Server backup failed during maintenance.",
  "priority": "High"
}
```

## What To Say

"The AI automatically creates a summary from the issue."

---

# 3. AI Recommendation Demo

## Input

```text
Database response time increased after deployment.
```

## What To Do
- Click AI Recommend

## Expected Output

```json
[
  {
    "action_type": "Performance",
    "description": "Check database indexes.",
    "priority": "High"
  }
]
```

## What To Say

"The AI gives recommendations to solve the issue."

---

# 4. AI Report Demo

## Input

```text
Multiple failed login attempts detected.
```

## What To Do
- Click Generate Report

## Expected Output

```json
{
  "title": "Security Incident Report",
  "summary": "Multiple failed logins detected."
}
```

## What To Say

"The AI creates a structured report automatically."

---

# 5. Health Endpoint Demo

Open:

```text
http://localhost:5000/health
```

Expected:

```json
{
  "status": "UP"
}
```

## What To Say

"This shows the AI service is running properly."

---

# 6. 60-Second Technical Explanation

Say:

"The frontend sends requests to the backend. The backend communicates with the Flask AI service. The AI service sends prompts to the Groq LLaMA model and returns AI-generated responses."

---

# 7. Security Talking Points

Say:

- JWT protects APIs
- Prompt injection is blocked
- Rate limiting prevents abuse
- Input sanitization prevents XSS

---

# 8. Backup Plan

If AI fails:
- Show screenshots
- Explain fallback response

Example:

```json
{
  "summary": "AI service unavailable",
  "is_fallback": true
}
```

---

# 9. Final Closing

Say:

"This tool automates procedure documentation using AI securely and efficiently."