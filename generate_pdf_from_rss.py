import xml.etree.ElementTree as ET
from datetime import datetime
from weasyprint import HTML

# Lire le fichier flux.xml
tree = ET.parse("flux.xml")
root = tree.getroot()

channel = root.find("channel")
items = channel.findall("item") if channel is not None else []

# Générer le HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weekly Press Review</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { text-align: center; }
        .article { margin-bottom: 30px; }
        .title { font-size: 18px; font-weight: bold; }
        .date { font-size: 12px; color: #555; }
        .description { margin-top: 5px; }
    </style>
</head>
<body>
    <h1>Weekly Press Review</h1>
"""

for item in items:
    title = item.findtext("title", default="(No title)")
    link = item.findtext("link", default="#")
    pub_date = item.findtext("pubDate", default="")
    description = item.findtext("description", default="")

    html_content += f"""
    <div class="article">
        <div class="title"><a href="{link}">{title}</a></div>
        <div class="date">{pub_date}</div>
        <div class="description">{description}</div>
    </div>
    """

html_content += "</body></html>"

# Sauvegarder le HTML
with open("weekly_press_review.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Convertir en PDF
HTML("weekly_press_review.html").write_pdf("weekly_press_review.pdf")

print("✅ PDF generated: weekly_press_review.pdf")