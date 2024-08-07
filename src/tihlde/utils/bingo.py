import os
import random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from PyPDF2 import PdfMerger

from tihlde.settings import (
    USER_DOWNLOAD_DIR,
    USER_TEMP_DIR
)


def generate_pdf(
    index: int,
    sentences: list[str],
    rows: int,
    cols: int,
):
    unique_sentences = list(set(sentences)) 
    directory = USER_TEMP_DIR

    if not os.path.exists(directory):
        os.mkdir(directory)

    pdf_file = f"{directory}/bingo{index + 1}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont("Helvetica", 10)

    CELL_WIDTH = 120
    CELL_HEIGHT = 120
    X_START = 5
    Y_START = 625

    random.shuffle(unique_sentences)

    for row in range(rows):
        for col in range(cols):
            sentence = unique_sentences.pop(0)

            x = X_START + col * CELL_WIDTH
            y = Y_START - row * CELL_HEIGHT

            c.rect(x, y, CELL_WIDTH, CELL_HEIGHT)

            max_chars = int(
                CELL_WIDTH / 6
            )

            lines = []
            current_line = ""
            for word in sentence.split():
                if len(current_line) + len(word) <= max_chars:
                    current_line += word + " "
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "
            if current_line:
                lines.append(current_line.strip())

            line_height = 20

            for i, line in enumerate(lines):
                c.drawString(
                    x + 10,
                    y + CELL_HEIGHT - (i * line_height) - 20,
                    line
                )

    c.save()


def merge_pdfs(name: str):
    merger = PdfMerger()
    pdf_folder = USER_TEMP_DIR
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            merger.append(file_path)
    
    merger.write(f"{USER_DOWNLOAD_DIR}/{name}.pdf")
    merger.close()
