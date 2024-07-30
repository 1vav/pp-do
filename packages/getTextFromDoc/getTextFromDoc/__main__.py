def main(args):
    import base64
    import pdfplumber
    from docx import Document
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
        # PDF files start with "%PDF"
        if file_data[:4] == b'%PDF':
            return 'pdf'
        # DOCX files have the "PK" signature (zip archive) and contain "[Content_Types].xml"
    elif file_data[:2] == b'PK' and b'[Content_Types].xml' in file_data:
            return 'docx'
        else:
            raise ValueError("Undetected file type " + str(file_data[:4]))

    def extract_text(base64_string):
        file_data = decode_base64(base64_string)
        file_type = detect_file_type(file_data)

        if file_type == 'pdf':
            return {"type": file_type, "text": extract_text_from_pdf(file_data)}
        elif file_type == 'docx':
            return {"type": file_type, "text": extract_text_from_docx(file_data)}
        else:
            raise ValueError("Unsupported file type" + file_type)

    # Example Usage
    base64_file = args.get("base64_file", "")  # base64-encoded file string

    try:
        type_and_text_from_file = extract_text(base64_file)
        print("Text from PDF:", type_and_text_from_file.text)
        return type_and_text_from_file
    except ValueError as e:
        print("Error:", str(e))
        return {"Error:": str(e)}
