import fitz

def redact_pdf(input_pdf, output_pdf, sensitive_data):

    doc = fitz.open(input_pdf)

    for page in doc:

        for item in sensitive_data:

            areas = page.search_for(item)

            for rect in areas:
                page.add_redact_annot(rect, fill=(0, 0, 0))

        page.apply_redactions()

    doc.save(output_pdf)