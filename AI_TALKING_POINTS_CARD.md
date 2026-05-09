# AI TALKING POINTS CARD

# 1. Project Introduction

Say:

"This project uses AI to generate descriptions, recommendations, and reports automatically."

---

# 2. What AI Technology Is Used?

Say:

"We used Flask, Groq API, and the LLaMA AI model."

Simple explanation:

- Flask → handles AI requests
- Groq → provides AI service
- LLaMA → generates AI responses

---

# 3. How Does The AI Work?

Say:

"The frontend sends data to the backend. The backend sends requests to the Flask AI service. The AI service sends prompts to Groq AI and receives responses."

---

# 4. What Is A Prompt?

Say:

"A prompt is an instruction given to the AI model."

Example:

Input:

```text
Server backup failed during maintenance.
```

Prompt:

```text
Generate a professional summary.
```

AI Output:

```text
Server backup process failed during maintenance.
```

---

# 5. AI Features

## AI Describe

Say:

"AI Describe creates summaries automatically."

---

## AI Recommend

Say:

"AI Recommend gives suggestions to solve issues."

---

## AI Generate Report

Say:

"AI Generate Report creates structured reports automatically."

---

# 6. Security Features

Say:

- JWT protects APIs
- Prompt injection is blocked
- SQL injection is blocked
- XSS attacks are prevented
- Rate limiting prevents abuse

---

# 7. Health Endpoint

Say:

"The /health endpoint shows the AI service is running."

Example:

```text
http://localhost:5000/health
```

---

# 8. Backup Plan

Say:

"If live AI fails, fallback responses and screenshots are available."

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

"This project combines AI automation, security, and modern web technologies to simplify procedure documentation."