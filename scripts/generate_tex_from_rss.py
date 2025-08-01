import csv
import feedparser
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import os

# Configuration
CSV_FILE = "client_rss_feeds_cleaned.csv"
TEX_OUTPUT = "press_review.tex"
TEMPLATE_DIR = "templates"
TEMPLATE_FILE = "press_review_template.tex"

# Date limite : 7 jours en arrière
now = datetime.utcnow()
seven_days_ago = now - timedelta(days=7)

# Collecte des articles par entreprise
company_articles = []

with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        company = row.get("Company", "Unnamed Company")
        rss_url = row.get("RSS Feed URL", "").strip()

        if not rss_url:
            continue

        feed = feedparser.parse(rss_url)
        if feed.bozo:
            continue

        recent_entries = []
        for entry in feed.entries:
            pub_date = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub_date:
                pub_datetime = datetime(*pub_date[:6])
                if pub_datetime >= seven_days_ago:
                    recent_entries.append({
                        "title": entry.get("title", "No title"),
                        "summary": entry.get("summary", ""),
                        "published": entry.get("published", "") or entry.get("updated", ""),
                        "link": entry.get("link", "")
                    })

        if recent_entries:
            company_articles.append({
                "company": company,
                "articles": recent_entries[:5]  # Limite à 5 articles
            })

# Préparation de l'environnement Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# Rendu du fichier LaTeX
rendered_tex = template.render(
    generated_date=now.strftime("%Y-%m-%d"),
    companies=company_articles
)

# Écriture du fichier .tex
with open(TEX_OUTPUT, "w", encoding="utf-8") as f:
    f.write(rendered_tex)

print(f"✅ Fichier LaTeX généré : {TEX_OUTPUT}")

