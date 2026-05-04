from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach

app = Flask(__name__)

# ✅ Step 1: Setup rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# 🚨 Step 2: Prompt injection detection keywords
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "act as",
    "bypass",
    "jailbreak"
]

# ✅ Step 3: Input sanitisation function
def sanitize_input(user_input):
    # Remove HTML
    cleaned = bleach.clean(user_input, strip=True)

    # Convert to lowercase for checking
    lower_input = cleaned.lower()

    # Detect prompt injection
    for pattern in BLOCKED_PATTERNS:
        if pattern in lower_input:
            return None

    return cleaned

# ✅ Step 4: API route
@app.route("/ask", methods=["POST"])
@limiter.limit("30 per minute")  # limit per endpoint
def ask():
    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Missing prompt"}), 400

    user_input = data["prompt"]

    # Sanitize input
    safe_input = sanitize_input(user_input)

    if not safe_input:
        return jsonify({"error": "Unsafe input detected"}), 400

    # Dummy response (replace with AI call)
    return jsonify({
        "message": "Safe input received",
        "cleaned_input": safe_input
    })

# ✅ Run app
if __name__ == "__main__":
    app.run(debug=True)

