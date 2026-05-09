import requests

print("Starting E2E Tests...\n")

# Backend Health
try:
    r = requests.get("http://localhost:8080/actuator/health")
    print("Backend Health:", r.status_code)
except Exception as e:
    print("Backend Failed:", e)

# AI Health
try:
    r = requests.get("http://localhost:5000/health")
    print("AI Health:", r.status_code)
except Exception as e:
    print("AI Failed:", e)

# AI Describe Endpoint
try:
    payload = {
        "text": "How to reset employee password"
    }

    r = requests.post(
        "http://localhost:5000/describe",
        json=payload
    )

    print("Describe Endpoint:", r.status_code)
    print(r.json())

except Exception as e:
    print("Describe Failed:", e)