from docx2pdf import convert

class Docx2PdfConverter:
    def __init__(self, word,pdf):
        self.word_file = word
        self.pdf_file = pdf
    
    def word2pdf_converter(self):
        # Convert the DOCX file to PDF
        return convert (self.word_file,self.pdf_file)
        # No need to return anything here, the file is sent within a Flask route
