import feedparser
from weasyprint import HTML
from datetime import datetime

# URL de ton flux RSS combiné
RSS_FEED_URL = "https://example.com/combined-feed.xml"  # 🔁 Remplace par ton URL réel

# Analyse du flux RSS
feed = feedparser.parse(RSS_FEED_URL)

# Construction du contenu HTML
html_content = """
<html>
<head>
    <meta charset='utf-8'>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        h1 { text-align: center; }
        h2 { color: #2c3e50; }
        p { margin-bottom: 1em; }
        a { color: #2980b9; text-decoration: none; }
        .article { margin-bottom: 2em; }
    </style>
</head>
<body>
    <h1>Weekly Press Review</h1>
"""

# Ajout des articles
for entry in feed.entries:
    title = entry.get("title", "No title")
    summary = entry.get("summary", "No summary")
    link = entry.get("link", "#")
    published = entry.get("published", "")
    html_content += f"""
    <div class='article'>
        <h2>{title}</h2>
        <p><em>{published}</em></p>
        <p>{summary}</p>
        <p><a href='{link}'>{link}</a></p>
    </div>
    """

# Fin du document HTML
html_content += """
</body>
</html>
"""

# Génération du PDF
HTML(string=html_content).write_pdf("Weekly_Press_Review.pdf")
print("PDF generated: Weekly_Press_Review.pdf")
