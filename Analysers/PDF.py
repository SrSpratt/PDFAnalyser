import fitz
import os
from .Counter import WordCounter


class PDFExtractor():
    
    def __init__(self, path):
        self.Path = path

    def ExtractPDF(self):
        self.ExtractedText = None
        self.NewPath = None
        text = ""
        try:
            doc = fitz.open(self.Path)
            for page in doc:
                text += page.get_text()

            self.NewPath = os.path.join("pdfs", "documento.pdf")
            self.ExtractedText = text
            return text
        except Exception as ex:
            print(f"Erro ao ler o PDF: {ex}")
            return None

    def PrintExtracted(self):
        if self.ExtractedText is None:
            raise Exception('Não foi possível extrair!')
        print("=========TEXTO EXTRAÍDO=========")
        print(self.ExtractedText[:500] + "\n[...]\n")

        with open("extractedText.txt", "w", encoding="utf-8") as file:
            file.write(self.ExtractedText)
        print("Texto salvo em 'extractedTex.txt'")

    def GenerateFrequencies(self):
        wordCounter = WordCounter(self.ExtractedText)
        wordCounter.GenerateText()