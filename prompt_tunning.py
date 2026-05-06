from groq import Groq

#  Your API key
client = Groq(api_key="groq_api_key")

prompt = "Summarize the text in 2-3 sentences with key points."

inputs = [
    "AI is used in healthcare to detect diseases early.",
    "Python is used for AI and web development.",
    "Machine learning learns from data.",
    "Cybersecurity protects systems.",
    "Cloud computing stores data online.",
    "Data science analyzes data.",
    "Blockchain secures transactions.",
    "IoT connects devices.",
    "Robotics automates work.",
    "AI helps in automation."
]

for i, text in enumerate(inputs):
    print(f"\n--- Test {i+1} ---")
    print("Input:", text)

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt + "\n\nText:\n" + text}
        ],
        model="llama-3.1-8b-instant"   #  FIXED MODEL
    )

    output = response.choices[0].message.content
    print("Output:", output)

    score = int(input("Enter score (0-10): "))

    if score < 7:
        print(" Improve prompt")
    else:
        print(" Good")