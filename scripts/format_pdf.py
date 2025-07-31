import fitz  # PyMuPDF

# Fichier source et de sortie
input_pdf = "Weekly_Press_Review.pdf"
output_pdf = "Weekly_Press_Review_Formatted.pdf"

# Ouvrir le PDF existant
doc = fitz.open(input_pdf)
new_doc = fitz.open()

# Paramètres de mise en page
margin = 50
page_width, page_height = fitz.paper_size("a4")
font_title = "helvetica-bold"
font_article = "helvetica"

# Traitement page par page
for page in doc:
    text = page.get_text("text")
    lines = text.splitlines()

    new_page = new_doc.new_page(width=page_width, height=page_height)
    cursor_y = margin

    for line in lines:
        if line.startswith("===") and line.endswith("==="):
            # Titre d'entreprise
            title = line.replace("=", "").strip()
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 30)
            new_page.insert_textbox(rect, title, fontname=font_title, fontsize=16, align=1, render_mode=3)
            cursor_y += 35

        elif line.startswith("•") or line.startswith("·"):
            # Titre d'article
            rect = fitz.Rect(margin + 10, cursor_y, page_width - margin, cursor_y + 20)
            new_page.insert_textbox(rect, line.strip(), fontname=font_article, fontsize=12, align=0)
            cursor_y += 20

        elif "http" in line:
            # Lien
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, line.strip(), fontname=font_article, fontsize=10, align=0, color=(0, 0, 1))
            cursor_y += 18

        elif line.strip() == "":
            cursor_y += 10

        else:
            # Résumé ou date
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, line.strip(), fontname=font_article, fontsize=11, align=0)
            cursor_y += 16

        if cursor_y > page_height - margin:
            new_page = new_doc.new_page(width=page_width, height=page_height)
            cursor_y = margin

# Sauvegarde
new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✅ Nouveau PDF formaté enregistré sous : {output_pdf}")
