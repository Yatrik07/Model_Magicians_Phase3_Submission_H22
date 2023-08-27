import flask
from flask import Flask, render_template, redirect, send_file, request
from werkzeug.utils import secure_filename
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
from ocr_text_extraction.convert_to_ocr import convert_to_ocr

def convert_image_to_pdf(input_image_path, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    image = Image.open(input_image_path)
    img_width, img_height = image.size
    c.drawImage(input_image_path, 0, 0, width=img_width, height=img_height)
    c.showPage()
    c.save()

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/upload_document")
def load_inner_page():
    return render_template("inner-page.html")

@app.route("/submit_document", methods = ["POST"])
def document_submit():
    if request.method == "POST":
        fileType = request.form["fileType"]
        recordType = request.form["recordType"]
        print(fileType, recordType)

        # fileUpload = request.form["fileUpload"]

        file = request.files["fileUpload"]
        print(type(file), file)

        if os.path.exists("documents") and os.path.isdir("documents"):
            pass
        else:
            os.mkdir("documents")
        global docName
        docName = "documents/" + str(secure_filename(f"document_{fileType}_{recordType}_{''.join(file.filename.split('.')[:-1])}." + str(file.filename.split(".")[-1])))
        file.save(docName)  # file.filename
        print(docName)

        if  fileType == "image":
            convert_image_to_pdf(docName, docName.replace( docName.split(".")[-1] , 'pdf'))

    print("D:/DAIICT Hackathon/"+docName , docName)
    convert_to_ocr( "D:/daiict_hackathon/documents" , docName[10:])

    ocrd_filename = ''.join(docName.split(".")[:-1]) + "-OCR" + ''.join(docName.split(".")[-1])
    print(ocrd_filename)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)