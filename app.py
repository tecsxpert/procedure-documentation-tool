from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach

# ✅ Step 1: Create Flask app
app = Flask(__name__)

# ✅ Step 2: Add rate limiter (30 requests per minute)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# 🚨 Step 3: Define blocked words (for security)
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "act as",
    "bypass",
    "jailbreak"
]

# ✅ Step 4: Sanitisation function
def sanitize_input(user_input):
    # Remove HTML tags
    cleaned = bleach.clean(user_input, strip=True)

    # Convert to lowercase
    lower_input = cleaned.lower()

    # Check for dangerous patterns
    for pattern in BLOCKED_PATTERNS:
        if pattern in lower_input:
            return None

    return cleaned

# ✅ Step 5: Create API route
@app.route("/ask", methods=["POST"])
@limiter.limit("30 per minute")   # limit per API
def ask():
    data = request.get_json()

    # Check if prompt exists
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing prompt"}), 400

    user_input = data["prompt"]

    # Sanitize input
    safe_input = sanitize_input(user_input)

    # If unsafe → block
    if not safe_input:
        return jsonify({"error": "Unsafe input detected"}), 400

    # Dummy response (replace later with Groq)
    return jsonify({
        "message": "Success",
        "cleaned_input": safe_input
    })

# ✅ Step 6: Run server
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)