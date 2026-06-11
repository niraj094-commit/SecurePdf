# SecurePDF

SecurePDF is a Python-based automated PDF redaction system that detects and masks Personally Identifiable Information (PII) such as emails, phone numbers, and Aadhaar numbers from PDF documents.

## Features

* Upload PDF files
* Extract text from PDFs
* Detect sensitive information using Regex
* Automatic PDF redaction
* OCR support for scanned PDFs
* Download secure redacted PDFs

## Tech Stack

* Python
* Flask
* PyMuPDF
* pytesseract
* pdf2image
* Regex
* HTML/CSS

## Installation

```bash
git clone https://github.com/niraj094-commit/SecurePdf.git
cd SecurePdf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Future Improvements

* AI-based PII detection
* Better OCR redaction
* User authentication
* Cloud deployment
* Drag & Drop upload UI

## Author

Niraj Kumar
