from flask import Flask, request, jsonify
import bleach
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Rate Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Prompt Injection Patterns
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "developer mode",
    "system prompt"
]

# Security Headers
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

# Home route
@app.route("/")
def home():
    return "Flask Server Running"

# Health check route
@app.route("/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Flask server is working"
    })

# Generate route
@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    # Empty Input Check
    if not data:
        return jsonify({
            "error": "No input data provided"
        }), 400

    text = data.get("text", "")

    # Empty Text Check
    if not text.strip():
        return jsonify({
            "error": "Empty input"
        }), 400

    # Sanitize Input
    clean_text = bleach.clean(text)

    # Prompt Injection Check
    for pattern in BLOCKED_PATTERNS:
        if pattern in clean_text.lower():
            return jsonify({
                "error": "Prompt injection detected"
            }), 400

    response = f"AI Response for: {clean_text}"

    return jsonify({
        "input": clean_text,
        "response": response
    })

# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)