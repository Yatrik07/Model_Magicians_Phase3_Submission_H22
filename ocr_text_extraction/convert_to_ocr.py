import subprocess

def convert_to_ocr(pdf_dir_path, pdf_name):
    """
    This function runs a Docker container to convert a scanned PDF to a searchable/OCR'd PDF.
    Docker Image used: leofcardoso/pdf2pdfocr:latest
    """
    """
    This function runs a Docker command using the subprocess module.
    """

    command = f"docker run --rm -v {pdf_dir_path}:/home/docker leofcardoso/pdf2pdfocr -i ./{pdf_name}"

    process = subprocess.Popen(command)

    process.wait()
    print("DONE", process)

# a = "D:/daiict_hackathon/documents"
# # b = "documents/document_pdf_xray_Non-text-searchable.pdf"
# b = "document_pdf_xray_Non-text-searchable.pdf"
# # b = b[10:]
# print(a,b)

# convert_to_ocr(a,b)
