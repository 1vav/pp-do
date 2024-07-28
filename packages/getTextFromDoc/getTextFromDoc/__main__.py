def main(args):
    import base64
    import pdfplumber
    from python-docx import Document
    from io import BytesIO
    import mimetypes

    def decode_base64(base64_string):
        return base64.b64decode(base64_string)

    def extract_text_from_pdf(file_data):
        with pdfplumber.open(BytesIO(file_data)) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def extract_text_from_docx(file_data):
        doc = Document(BytesIO(file_data))
        return "\n".join([para.text for para in doc.paragraphs])

    def detect_file_type(file_data):
        mime = mimetypes.guess_type(BytesIO(file_data).name)[0]
        if mime == 'application/pdf':
            return 'pdf'
        elif mime == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            return 'docx'
        else:
            raise ValueError("Unsupported file type")

    def extract_text(base64_string):
        file_data = decode_base64(base64_string)
        file_type = detect_file_type(file_data)

        if file_type == 'pdf':
            return {"type": file_type, "text": extract_text_from_pdf(file_data)}
        elif file_type == 'docx':
            return {"type": file_type, "text": extract_text_from_docx(file_data)}
        else:
            raise ValueError("Unsupported file type")

    # Example Usage
    base64_file = args.get("file", "")  # base64-encoded file string

    try:
        type_and_text_from_file = extract_text(args.base64_file)
        print("Text from PDF:", type_and_text_from_file.text)
        return type_and_text_from_file
    except ValueError as e:
        print("Error:", e)
        return {"Error:": e}