import requests

BASE_URL = "http://localhost:8080"

sample_input = {
    "text": "How to install software safely"
}


def test_endpoint(endpoint):
    try:
        response = requests.post(
            f"{BASE_URL}/{endpoint}",
            json=sample_input
        )

        print(f"\nTesting /{endpoint}")
        print("Status Code:", response.status_code)

        try:
            print(response.json())
        except:
            print(response.text)

    except Exception as e:
        print("ERROR:", e)


test_endpoint("describe")
test_endpoint("recommend")
test_endpoint("generate-report")