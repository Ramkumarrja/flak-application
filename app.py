from flask import Flask, render_template, request,send_file
from word2pdfconverter import Docx2PdfConverter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    file = request.files['file']
    file.save('input.docx')
    word_output = 'uploads/output.pdf'
    converter = Docx2PdfConverter("input.docx",word_output)
    converter.convert_docx_to_pdf_linux()
    return send_file(
        word_output,
        as_attachment=True,
        download_name='output_document.pdf',
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
