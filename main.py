from Analysers import PDFExtractor
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrai texto de um PDF")
    parser.add_argument(
        "path",
        type=str,
        help="Caminho completo do PDF"
    )
    args = parser.parse_args()

    print(args.path)
    extractor = PDFExtractor(args.path)
    extractor.ExtractPDF()
    extractor.PrintExtracted()
    extractor.GenerateFrequencies()