import csv
import feedparser
import fitz  # PyMuPDF
from datetime import datetime, timedelta
import textwrap
import re

# Fichiers d'entrée et de sortie
csv_file = "client_rss_feeds_cleaned.csv"
pdf_output = "Weekly_Press_Review.pdf"
log_output = "rss_debug_log.txt"

# Initialisation du document PDF
pdf_doc = fitz.open()
log_lines = []

# Date limite : 7 jours en arrière
now = datetime.utcnow()
seven_days_ago = now - timedelta(days=7)

# Fonction pour détecter les liens illisibles (ex: Google News)
def is_unreadable_link(url):
    return "news.google.com/rss/articles/" in url or len(url) > 150

# Lecture du fichier CSV
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        company = row.get("Company", "Unnamed Company")
        rss_url = row.get("RSS Feed URL", "").strip()

        if not rss_url:
            log_lines.append(f"[{company}] ❌ Aucun flux RSS fourni.")
            continue

        feed = feedparser.parse(rss_url)

        if feed.bozo:
            log_lines.append(f"[{company}] ❌ Erreur de parsing du flux RSS : {feed.bozo_exception}")
            continue

        # Filtrer les articles récents
        recent_entries = []
        for entry in feed.entries:
            pub_date = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub_date:
                pub_datetime = datetime(*pub_date[:6])
                if pub_datetime >= seven_days_ago:
                    recent_entries.append(entry)

        article_count = len(recent_entries)

        if article_count == 0:
            log_lines.append(f"[{company}] ⚠️ Aucun article publié dans les 7 derniers jours.")
        else:
            log_lines.append(f"[{company}] ✅ {article_count} article(s) récents récupéré(s).")

        # Création d'une page PDF pour cette entreprise
        page = pdf_doc.new_page()
        text = f"=== {company} ===\n\n"

        if article_count == 0:
            text += "No recent articles available.\n"
        else:
            for entry in recent_entries[:5]:  # Limite à 5 articles
                title = entry.get("title", "No title")
                summary = entry.get("summary", "")
                published = entry.get("published", "") or entry.get("updated", "")
                link = entry.get("link", "")

                # Nettoyage du résumé : suppression de "Read more" et balises HTML
                summary_clean = re.sub(r'<[^>]+>', '', summary)
                summary_clean = re.sub(r'Read more\s*$', '', summary_clean, flags=re.IGNORECASE)

                # Lien replié proprement s'il est lisible
                if link and not is_unreadable_link(link):
                    wrapped_link = "\n".join(textwrap.wrap(link, width=80, break_long_words=True))
                    text += f"• {title}\n  {published}\n  {summary_clean}\n  {wrapped_link}\n\n"
                else:
                    text += f"• {title}\n  {published}\n  {summary_clean}\n\n"

        page.insert_text((72, 72), text, fontsize=11)

# Sauvegarde du PDF
pdf_doc.save(pdf_output)
pdf_doc.close()

# Sauvegarde du fichier de log
with open(log_output, "w", encoding="utf-8") as log_file:
    log_file.write(f"RSS Debug Log - {now.isoformat()}\n\n")
    log_file.write("\n".join(log_lines))

print(f"✅ PDF généré : {pdf_output}")
print(f"🧾 Log généré : {log_output}")
