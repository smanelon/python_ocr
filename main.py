from extract import extract_pdf_text_preserve_rows

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(extract_pdf_text_preserve_rows(sys.argv[1]))

# Neuer Commentar