import fitz

def extract_pdf_text(file_path: str) -> str:
    """Liest eine PDF-Datei ein und gibt den gesamten Text zurück.

    Args:
        file_path: Pfad zur PDF-Datei.

    Returns:
        Vollständiger Textinhalt der PDF-Datei.
    """
    text_parts = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text_parts.append(page.get_text())
    return "".join(text_parts)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(extract_pdf_text(sys.argv[1]))
