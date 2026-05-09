# SECURITY.md

# Tool-32 Procedure Documentation Tool
## Final Security Report

---

# 1. Introduction

This document explains the security features added to the project.

The project was tested for common attacks like:

- SQL Injection
- Prompt Injection
- XSS
- Unauthorized Access
- API Abuse

All major security problems were fixed before Demo Day.

---

# 2. JWT Authentication

The backend uses JWT tokens for login security.

Protected APIs need a valid token.

If the token is missing or invalid:

- User gets 401 Unauthorized error

Example protected features:

- Create record
- Update record
- Delete record
- AI endpoints

---

# 3. Prompt Injection Protection

The AI service blocks dangerous prompts.

Blocked examples:

- ignore previous instructions
- developer mode
- reveal secrets
- bypass restrictions

If detected:

- Request returns 400 Bad Request

This protects the AI model from misuse.

---

# 4. Input Validation

All user input is checked before processing.

Protection includes:

- Empty input check
- Invalid JSON check
- HTML cleaning
- Dangerous script removal

Example blocked input:

```html
