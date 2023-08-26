import fitz

def extract_text_from_pdf(input_path):
    pdf = fitz.open(input_path)
    total_pages = pdf.page_count  # Get the total number of pages in the PDF

    txt = ''
    for i in range(total_pages):
        pg = pdf.load_page(i)
        txt += pg.get_text()
    return txt

