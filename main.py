from extract import extract_pdf_text_preserve_rows
import os

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        pdf_path = sys.argv[1]
        output_path = sys.argv[2]
        text = extract_pdf_text_preserve_rows(pdf_path)
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
    else:
        print("Usage: python main.py <pdf_path> <output_file>")

# Neuer Commentar