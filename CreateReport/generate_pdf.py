
from reportlab.pdfgen import canvas

def create_pdf():
    name = "Krushn"
    text =    """
    ಕನ್ನಡದಲ್ಲಿ{name} ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n|
    ಕನ್ನಡದಲ್ಲಿ ಪೈಥಾನ್ ತರಬೇತಿ \n
    """
    c = canvas.Canvas("simple_pdf.pdf")
    c.drawString(100, 750, "Hello, I am a PDF document created with Python!\n"+text)
    c.save()

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_kannada_pdf(file_path):
    # Register Kannada font (Lohit-Kannada.ttf is just an example, you can replace it with the path to your Kannada font)
    pdfmetrics.registerFont(TTFont('Kannada', 'Lohit_Kannada_Regular.ttf'))

    # Create a PDF document
    c = canvas.Canvas(file_path)

    # Set the font for Kannada text
    c.setFont('Kannada', 12)

    # Add Kannada text to the PDF
    kannada_text = "ಹಲೋ, ಈ ಒಂದು ಕನ್ನಡ ಪಿಡಿಎಫ್ ಆಗಿದೆ!"
    c.drawString(100, 700, kannada_text)

    # Save the PDF
    c.save()

# Example usage:
pdf_file_path = "kannada_example.pdf"
create_kannada_pdf(pdf_file_path)

if __name__ == "__main__":
    # create_pdf()
    create_pdf()