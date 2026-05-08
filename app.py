from flask import Flask, request, jsonify

app = Flask(__name__)

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

    if not data:
        return jsonify({
            "error": "No input data provided"
        }), 400

    text = data.get("text", "")

    response = f"AI Response for: {text}"

    return jsonify({
        "input": text,
        "response": response
    })

# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)