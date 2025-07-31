import fitz  # PyMuPDF

# Fichier source et de sortie
input_pdf = "Weekly_Press_Review.pdf"
output_pdf = "Weekly_Press_Review_Formatted.pdf"

# Ouvrir le PDF existant
doc = fitz.open(input_pdf)
new_doc = fitz.open()

# Paramètres de mise en page
margin = 72  # 1 inch
page_width = 595  # A4 width in points
page_height = 842  # A4 height in points
text_width = page_width - 2 * margin
font = "Times-Italic"

# Reformatage de chaque page
for page in doc:
    text = page.get_text()

    # Nouvelle page
    new_page = new_doc.new_page()

    # Zone de texte
    rect = fitz.Rect(margin, margin, page_width - margin, page_height - margin)

    # Insertion du texte avec centrage
    new_page.insert_textbox(rect, text, fontsize=11, fontname=font, align=1)

# Sauvegarde
new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✅ Nouveau PDF formaté enregistré sous : {output_pdf}")
