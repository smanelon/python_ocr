import fitz
from statistics import median

def extract_pdf_text_preserve_rows(path: str, col_sep: str = "\t", y_tol: float = 2.0) -> str:
    doc = fitz.open(path)
    all_lines = []

    for page in doc:
        words = page.get_text("words")  # (x0, y0, x1, y1, word, block_no, line_no, word_no)
        if not words:
            continue

        # Sortiere nach Y, dann X
        words.sort(key=lambda w: (round(w[1],1), w[0]))

        # Gruppiere nach Y-Koordinate mit Toleranz
        rows = []
        current_row = []
        current_y = None
        for x0, y0, x1, y1, text, *_ in words:
            if current_y is None or abs(y0 - current_y) <= y_tol:
                current_row.append((x0, text))
                current_y = y0 if current_y is None else (current_y + y0)/2
            else:
                rows.append(current_row)
                current_row = [(x0, text)]
                current_y = y0
        if current_row:
            rows.append(current_row)

        # baue jede Zeile
        for row in rows:
            row = sorted(row, key=lambda t: t[0])
            # Abstände prüfen, um Spalten zu trennen
            pieces = []
            prev_x = None
            gaps = []
            for x, text in row:
                if prev_x is None:
                    pieces.append(text)
                else:
                    gap = x - prev_x
                    gaps.append(gap)
                    if gap > 5:  # Schwelle für Tab/Spaltentrenner
                        pieces.append(col_sep + text)
                    else:
                        pieces.append(" " + text)
                prev_x = x + len(text)*3  # grob schätzen Breite
            all_lines.append("".join(pieces))

    doc.close()
    return "\n".join(all_lines)

# Test
# pdf_path = "/mnt/data/5548_beitragsrechnung_16e4e404-16cd-4b0f-87dd-3a5cfa6b1c14.pdf"
# text = extract_pdf_text_preserve_rows(pdf_path)
# print(text.splitlines()[50:65])  # Stelle mit 'Versicherungsart' usw. zeigen
