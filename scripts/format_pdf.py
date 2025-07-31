import fitz  # PyMuPDF
import textwrap

# Nom du fichier PDF d'entrée et de sortie
input_pdf = "Weekly_Press_Review.pdf"
output_pdf = "Weekly_Press_Review_Formatted.pdf"

# Ouvrir le PDF existant
doc = fitz.open(input_pdf)

# Créer un nouveau document PDF pour la version formatée
new_doc = fitz.open()

# Définir les marges et la largeur de texte
margin = 72  # 1 pouce
page_width = fitz.paper_size("a4")[0]
usable_width = page_width - 2 * margin

# Définir les polices
font = "helv"

# Parcourir chaque page du PDF original
for page in doc:
    text = page.get_text("text")
    lines = text.splitlines()

    new_page = new_doc.new_page()
    cursor_y = margin

    for line in lines:
        line = line.strip()
        if not line:
            cursor_y += 10
            continue

        # Titre d'entreprise
        if line.startswith("===") and line.endswith("==="):
            company = line.strip("= ").upper()
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 20)
            new_page.insert_textbox(rect, company, fontsize=16, fontname=font, align=1, render_mode=3)
            cursor_y += 30
            continue

        # Titre d'article
        if line.startswith("• "):
            title = line[2:]
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, "• " + title, fontsize=12, fontname=font, render_mode=3)
            cursor_y += 20
            continue

        # Date
        if line[:3] in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 12)
            new_page.insert_textbox(rect, line, fontsize=10, fontname=font, italic=True)
            cursor_y += 15
            continue

        # Lien (centré)
        if line.startswith("http"):
            wrapped = textwrap.wrap(line, width=90)
            for wrapped_line in wrapped:
                rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 10)
                new_page.insert_textbox(rect, wrapped_line, fontsize=9, fontname=font, align=1)
                cursor_y += 12
            continue

        # Résumé ou texte normal
        wrapped = textwrap.wrap(line, width=100)
        for wrapped_line in wrapped:
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 12)
            new_page.insert_textbox(rect, wrapped_line, fontsize=10, fontname=font)
            cursor_y += 14

        # Ajouter un espace après chaque bloc
        cursor_y += 6

# Sauvegarder le nouveau PDF
new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✅ PDF formaté enregistré sous : {output_pdf}")
