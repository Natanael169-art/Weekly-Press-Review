import fitz  # PyMuPDF

input_pdf = "weekly_press_review 10.pdf"
output_pdf = "weekly_press_review_Formatted.pdf"

doc = fitz.open(input_pdf)
new_doc = fitz.open()

page_width, page_height = fitz.paper_size("a4")
margin = 50
font_title = "helvetica-bold"
font_article = "helvetica"

for page in doc:
    text = page.get_text("text")
    lines = text.splitlines()

    new_page = new_doc.new_page(width=page_width, height=page_height)
    cursor_y = margin

    for line in lines:
        line = line.strip()

        if line.startswith("===") and line.endswith("==="):
            title = line.replace("=", "").strip()
            rect = fitz.Rect(margin, cursor_y, page_width - margin, cursor_y + 30)
            new_page.insert_textbox(rect, title, fontname=font_title, fontsize=16, align=1, render_mode=3)
            cursor_y += 35

        elif line.startswith("·") or line.startswith("•"):
            rect = fitz.Rect(margin + 10, cursor_y, page_width - margin, cursor_y + 20)
            new_page.insert_textbox(rect, line.strip("·• "), fontname=font_article, fontsize=12, align=0)
            cursor_y += 20

        elif "http" in line:
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, line, fontname=font_article, fontsize=10, color=(0, 0, 1))
            cursor_y += 18

        elif line == "":
            cursor_y += 8

        else:
            rect = fitz.Rect(margin + 20, cursor_y, page_width - margin, cursor_y + 15)
            new_page.insert_textbox(rect, line, fontname=font_article, fontsize=11)
            cursor_y += 16

        if cursor_y > page_height - margin:
            new_page = new_doc.new_page(width=page_width, height=page_height)
            cursor_y = margin

new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✅ Nouveau PDF formaté enregistré sous : {output_pdf}")
