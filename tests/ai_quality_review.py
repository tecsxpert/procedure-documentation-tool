import requests
import json

BASE_URL = " http://127.0.0.1:8080"

# 10 test inputs per endpoint
describe_inputs = [
    "Patient has fever and cough",
    "Broken leg injury procedure",
    "Server deployment steps",
    "Blood pressure measurement process",
    "Login authentication flow",
    "Database backup procedure",
    "MRI scan procedure",
    "Email sending workflow",
    "API request lifecycle",
    "Docker container startup process"
]

recommend_inputs = [
    "Improve hospital workflow",
    "Fix slow backend system",
    "Optimize database queries",
    "Reduce patient waiting time",
    "Improve security system",
    "Automate report generation",
    "Enhance UI performance",
    "Improve cloud deployment",
    "Reduce system downtime",
    "Improve API reliability"
]

report_inputs = [
    "Hospital management system",
    "E-commerce platform performance",
    "Banking application overview",
    "AI medical assistant system",
    "Smart traffic control system",
    "Online learning platform",
    "Inventory management system",
    "Cybersecurity monitoring tool",
    "Food delivery system",
    "Smart home automation system"
]


def score_output(text):
    """
    Simple heuristic scoring (1–5)
    """
    if not text:
        return 1
    if len(text) < 50:
        return 2
    if "error" in text.lower():
        return 2
    if len(text) > 200:
        return 5
    return 4


def test_endpoint(endpoint, inputs):
    print(f"\n🔹 Testing {endpoint} endpoint")

    scores = []

    for i, inp in enumerate(inputs):
        try:
            response = requests.post(
                f"{BASE_URL}/{endpoint}",
                json={"input": inp},
                timeout=10
            )

            print(f"\nTest {i+1} Status Code:", response.status_code)

            #  SAFE JSON PARSING
            try:
                data = response.json()
                output = json.dumps(data)
            except Exception:
                print("⚠️ Non-JSON Response:", response.text)
                output = response.text

            score = score_output(output)
            scores.append(score)

            print(f"Test {i+1}: Score = {score}")

        except Exception as e:
            print(f"Test {i+1}: Failed - {e}")
            scores.append(1)

    avg = sum(scores) / len(scores)
    print(f"\n✅ {endpoint.upper()} AVG SCORE: {avg:.2f}")

    return avg


if __name__ == "__main__":
    describe_score = test_endpoint("describe", describe_inputs)
    recommend_score = test_endpoint("recommend", recommend_inputs)
    report_score = test_endpoint("generate-report", report_inputs)

    print("\n========================")
    print("FINAL AI QUALITY REPORT")
    print("========================")
    print(f"Describe Avg Score: {describe_score:.2f}")
    print(f"Recommend Avg Score: {recommend_score:.2f}")
    print(f"Report Avg Score: {report_score:.2f}")