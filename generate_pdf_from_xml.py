from fpdf import FPDF
import re

# Charger le fichier XML brut
with open("flux.xml", "r", encoding="utf-8") as f:
    content = f.read()

# Extraire les articles avec des expressions régulières
articles = re.findall(
    r'<a href="([^"]+)".*?>(.*?)</a>.*?<font color="[^"]+">(.*?)</font>.*?(\w{3}, \d{2} \w{3} \d{4}.*?) \+0000',
    content,
    re.DOTALL
)

# Créer le PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Weekly Press Review", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
for link, title, source, date in articles:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, f"Title: {title.strip()}")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Date: {date.strip()}")
    pdf.multi_cell(0, 10, f"Source: {source.strip()}")
    pdf.multi_cell(0, 10, f"Link: {link.strip()}")
    pdf.ln(5)

pdf.output("weekly_press_review.pdf")
print("✅ PDF généré : weekly_press_review.pdf")
