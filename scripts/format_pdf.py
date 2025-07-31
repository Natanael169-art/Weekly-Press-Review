import fitz  # PyMuPDF
from bs4 import BeautifulSoup

input_pdf = "weekly_press_review 10.pdf"
output_pdf = "weekly_press_review_Formatted.pdf"

doc = fitz.open(input_pdf)
new_doc = fitz.open()

page_width, page_height = fitz.paper_size("a4")
margin = 50
font_title = "helvetica-bold"
font_article = "helvetica"

for page in doc:
    html = page.get_text("html")
    soup = BeautifulSoup(html, "html.parser")

    new_page = new_doc.new_page(width=page_width, height=page_height)
    cursor_y = margin

    for tag in soup.find_all(["p", "a", "font"]):
        text = tag.get_text(strip=True)
        if not text:
            continue

        if text.startswith("===") and text.endswith("==="):
            # Titre d'entreprise
            title = text.replace("=", "").strip()
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 30)
            new_page.insert_textbox(rect, title, fontname=font_title, fontsize=16, align=1, render_mode=3)
            cursor_y += 35

        elif text.startswith("·") or text.startswith("•"):
            # Titre d'article
            rect = fitz.Rect(margin + 10, cursor_y, page_width - margin, cursor_y + 20)
            new_page.insert_textbox(rect, text.strip("·• "), fontname=font_article, fontsize=12)
            cursor_y += 20

        elif "http" in text:
            # Lien
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, text, fontname=font_article, fontsize=10, color=(0, 0, 1))
            cursor_y += 18

        else:
            # Résumé ou date
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, text, fontname=font_article, fontsize=11)
            cursor_y += 16

        if cursor_y > page_height - margin:
            new_page = new_doc.new_page(width=page_width, height=page_height)
            cursor_y = margin

new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✅ Nouveau PDF formaté enregistré sous : {output_pdf}")
