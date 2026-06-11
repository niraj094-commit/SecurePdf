from ocr import extract_text_ocr
from flask import Flask, render_template, request
from detector import extract_text, detect_pii
from redactor import redact_pdf
from flask import send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        file = request.files['pdf']
        if not file.filename.endswith(".pdf"):
            return "Please upload a valid PDF file"

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            text = extract_text(filepath)
            if not text.strip():
                text = extract_text_ocr(filepath)
            detected = detect_pii(text)

            sensitive_items = []

            for values in detected.values():
                sensitive_items.extend(values)

            output_path = os.path.join("output", "redacted.pdf")

            redact_pdf(filepath, output_path, sensitive_items)

            return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
   app.run(debug=True, port=8001)