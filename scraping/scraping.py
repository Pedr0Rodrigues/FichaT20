import PyPDF2

from PyPDF2 import PdfReader

def text_pdf_all_pages (filepath):
    text = ''
    reader = PdfReader (filepath)
    number_of_pages = len(reader.pages)
    for i in range (number_of_pages):
        page = reader.pages[i]
        text += page.extract_text()
    return text

def text_pdf_some_pages (filepath, pageStart, pageEnd):
    text = ''
    reader = PdfReader (filepath)
    for i in range (pageStart-1, pageEnd):
        page = reader.pages[i]
        text += page.extract_text() 
    return text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

#Para a parte de Poderes do livro básico
save_text_to_file(text_pdf_some_pages("arquivos/jogo_do_ano_1.2.pdf",130,143),"arquivos/poderes.txt")

