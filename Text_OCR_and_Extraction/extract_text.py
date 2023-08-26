import fitz

input_path = r"D:\Yatrik Shah Backup\Downloads\Non-text-searchable.pdf"
output_path = r"outputs/ocrmypdf.pdf"

pdf = fitz.open(input_path)

txt = ''
for i in range(total_pages):
    pg = pdf.load_page(i)    
    txt += pg.get_text()
    return txt

print(txt)