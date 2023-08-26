import docker

def main():
    """
    This function runs a Docker container using the docker module.
    That container creates a searchable / OCR'd pdf from a scanned pdf.
    Docker Image used: leofcardoso/pdf2pdfocr:latest
    
    This is definitely better than 'Pytesseract' and 'OCRmyPDF' libraries, manually tested and can prove ...
    """

    client = docker.from_env()

    path_to_pdf_dir = r"D:\python_projects\cloudoffice-job\poc_project1\NON_OCR1"
    pdf_name = r"2_Dave-Non_OCR.pdf"

    container = client.containers.create(
        image="leofcardoso/pdf2pdfocr:latest",
        command=f'docker run --rm -v "{path_to_pdf_dir}:/home/docker" leofcardoso/pdf2pdfocr -v -i ./{pdf_name}'
    )

    container.start()

if __name__ == "__main__":
    main()