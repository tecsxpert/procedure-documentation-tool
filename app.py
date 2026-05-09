from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach

app = Flask(__name__)

# =========================
# RATE LIMITER
# =========================
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# =========================
# SECURITY FILTERS
# =========================

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "developer mode",
    "system prompt",
    "reveal prompt",
    "bypass security",
    "jailbreak"
]


def sanitize_input(text):
    """
    Cleans HTML/JS from input
    """
    if not isinstance(text, str):
        return ""

    cleaned = bleach.clean(text)

    return cleaned.strip()


def detect_prompt_injection(text):
    """
    Detect suspicious prompt injection attempts
    """
    lower_text = text.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in lower_text:
            return True

    return False


# =========================
# AI LOGIC FUNCTIONS
# =========================

def generate_description(text):
    """
    Generate detailed procedure description
    """

    response = f"""
Procedure Description

Objective:
{text}

Detailed Steps:
1. Review the provided procedure carefully.
2. Prepare all required tools and resources.
3. Execute each step in the correct order.
4. Validate the output after completion.
5. Record any issues or observations.

Safety Notes:
- Follow standard safety guidelines.
- Verify configurations before execution.
- Ensure proper documentation.

Expected Result:
The procedure should complete successfully with verified output.
"""

    return response.strip()


def generate_recommendation(text):
    """
    Generate recommendations
    """

    response = f"""
Recommendations for Procedure

Based on the provided input:
{text}

Recommended Actions:
1. Improve documentation clarity.
2. Add validation checks before execution.
3. Include error-handling procedures.
4. Maintain backup and recovery steps.
5. Perform final verification after completion.

Quality Improvements:
- Use structured instructions.
- Reduce ambiguity in steps.
- Add monitoring and logging where necessary.
"""

    return response.strip()


def generate_report(text):
    """
    Generate structured report
    """

    response = {
        "summary": f"Procedure analysis completed for: {text}",

        "steps": [
            "Input reviewed",
            "Procedure analyzed",
            "Safety checks evaluated",
            "Recommendations generated",
            "Final report prepared"
        ],

        "risks": [
            "Configuration mismatch",
            "Human operational error",
            "Insufficient validation"
        ],

        "recommendations": [
            "Add automated validation",
            "Improve documentation",
            "Perform regular audits"
        ],

        "status": "SUCCESS"
    }

    return response


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return jsonify({
        "message": "AI Procedure Documentation Tool Running"
    })


# -------------------------
# DESCRIBE ENDPOINT
# -------------------------
@app.route("/describe", methods=["POST"])
@limiter.limit("10 per minute")
def describe():

    data = request.get_json()

    print("REQUEST DATA:", data)

    text = sanitize_input(data.get("text", ""))

    if detect_prompt_injection(text):
        return jsonify({
            "error": "Prompt injection attempt detected"
        }), 400

    result = generate_description(text)

    print("AI RESULT:", result)

    return jsonify({
        "description": result
    })


# -------------------------
# RECOMMEND ENDPOINT
# -------------------------
@app.route("/recommend", methods=["POST"])
@limiter.limit("10 per minute")
def recommend():

    data = request.get_json()

    print("REQUEST DATA:", data)

    text = sanitize_input(data.get("text", ""))

    if detect_prompt_injection(text):
        return jsonify({
            "error": "Prompt injection attempt detected"
        }), 400

    result = generate_recommendation(text)

    print("AI RESULT:", result)

    return jsonify({
        "recommendation": result
    })


# -------------------------
# GENERATE REPORT ENDPOINT
# -------------------------
@app.route("/generate-report", methods=["POST"])
@limiter.limit("10 per minute")
def generate_report_endpoint():

    data = request.get_json()

    print("REQUEST DATA:", data)

    text = sanitize_input(data.get("text", ""))

    if detect_prompt_injection(text):
        return jsonify({
            "error": "Prompt injection attempt detected"
        }), 400

    result = generate_report(text)

    print("AI RESULT:", result)

    return jsonify(result)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )