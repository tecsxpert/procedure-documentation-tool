import re

def remove_pii(text):
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    return text


#  THIS PART IS REQUIRED TO SEE OUTPUT
if __name__ == "__main__":
    sample_text = "Call 9876543210 or mail test@gmail.com"
    result = remove_pii(sample_text)
    print(result)