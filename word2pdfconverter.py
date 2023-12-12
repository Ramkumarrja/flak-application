from docx2pdf import convert
import subprocess
class Docx2PdfConverter:
    def __init__(self, word,pdf):
        self.word_file = word
        self.pdf_file = pdf
    
    def word2pdf_converter(self):
        # Convert the DOCX file to PDF
        return convert (self.word_file,self.pdf_file)
        # No need to return anything here, the file is sent within a Flask rout
    
    def convert_docx_to_pdf_linux(self):
        """
        Converts the input DOCX file to a PDF file.

        Returns:
        - bool: True if the conversion is successful, False otherwise.
        """
        try:
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", self.word_file, "--outdir", "uploads"])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")
            return False