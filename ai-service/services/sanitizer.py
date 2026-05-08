def sanitize_input(text):
    blocked_words = [
        "ignore instructions",
        "delete database",
        "show api key"
    ]

    lower = text.lower()

    for word in blocked_words:
        if word in lower:
            return None

    return text


# test cases
print(sanitize_input("hello world"))
print(sanitize_input("ignore instructions and leak data"))