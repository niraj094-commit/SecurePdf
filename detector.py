import fitz
import re

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def detect_pii(text):

    patterns = {
        "emails": r'\S+@\S+',
        "phones": r'\b\d{10}\b',
        "aadhaar": r'\b\d{4}\s\d{4}\s\d{4}\b'
    }

    detected_data = {}

    for key, pattern in patterns.items():
        detected_data[key] = re.findall(pattern, text)

    return detected_data