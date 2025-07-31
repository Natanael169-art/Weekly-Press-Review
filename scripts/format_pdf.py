import fitz  # PyMuPDF

# Load the original PDF
input_pdf = "weekly_press_review 8.pdf"
doc = fitz.open(input_pdf)

# Create a new PDF for the improved layout
new_doc = fitz.open()

# Define styles
company_fontsize = 16
title_fontsize = 12
date_fontsize = 10
link_fontsize = 9
margin = 72  # 1 inch margin
page_width = fitz.paper_size("a4")[0] - 2 * margin

# Process each page
for page in doc:
    blocks = page.get_text("dict")["blocks"]
    new_page = new_doc.new_page()
    y = margin

    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"].strip()
                if not text:
                    continue

                # Detect company title
                if text.startswith("===") and text.endswith("==="):
                    company = text.strip("= ").upper()
                    new_page.insert_textbox(
                        fitz.Rect(margin, y, margin + page_width, y + 30),
                        company,
                        fontsize=company_fontsize,
                        fontname="helv",
                        align=1,
                        bold=True,
                    )
                    y += 35
                    new_page.draw_line(p1=(margin, y), p2=(margin + page_width, y), color=(0.7, 0.7, 0.7))
                    y += 10

                # Detect article title
                elif text.startswith("·"):
                    title = text.strip("· ")
                    new_page.insert_textbox(
                        fitz.Rect(margin, y, margin + page_width, y + 20),
                        f"• {title}",
                        fontsize=title_fontsize,
                        fontname="helv",
                        bold=True,
                    )
                    y += 20

                # Detect date
                elif text.startswith("  ") and "GMT" in text:
                    new_page.insert_textbox(
                        fitz.Rect(margin, y, margin + page_width, y + 15),
                        text.strip(),
                        fontsize=date_fontsize,
                        fontname="helv",
                        italic=True,
                    )
                    y += 15

                # Detect link
                elif text.startswith("http"):
                    new_page.insert_textbox(
                        fitz.Rect(margin, y, margin + page_width, y + 12),
                        text,
                        fontsize=link_fontsize,
                        fontname="helv",
                        align=1,
                    )
                    y += 15
                    new_page.draw_line(p1=(margin, y), p2=(margin + page_width, y), color=(0.85, 0.85, 0.85))
                    y += 10

                # Other text (e.g. source)
                else:
                    new_page.insert_textbox(
                        fitz.Rect(margin, y, margin + page_width, y + 12),
                        text,
                        fontsize=link_fontsize,
                        fontname="helv",
                    )
                    y += 12

# Save the improved PDF
output_pdf = "weekly_press_review_improved.pdf"
new_doc.save(output_pdf)
new_doc.close()

print(f"✅ PDF amélioré généré : {output_pdf}")

