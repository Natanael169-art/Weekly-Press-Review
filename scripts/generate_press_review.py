import csv
import feedparser
import fitz  # PyMuPDF
from datetime import datetime

# Fichiers d'entrée et de sortie
csv_file = "client_rss_feeds_cleaned.csv"
pdf_output = "Weekly_Press_Review.pdf"
log_output = "rss_debug_log.txt"

# Initialisation du document PDF
pdf_doc = fitz.open()
log_lines = []

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

        entries = feed.entries
        article_count = len(entries)

        if article_count == 0:
            log_lines.append(f"[{company}] ⚠️ Aucun article trouvé.")
        else:
            log_lines.append(f"[{company}] ✅ {article_count} article(s) récupéré(s).")

        # Création d'une page PDF pour cette entreprise
        page = pdf_doc.new_page()
        text = f"=== {company} ===\n\n"

        if article_count == 0:
            text += "No articles available.\n"
        else:
            for entry in entries[:5]:  # Limite à 5 articles par entreprise
                title = entry.get("title", "No title")
                link = entry.get("link", "")
                summary = entry.get("summary", "")
                published = entry.get("published", "") or entry.get("updated", "")
                text += f"• {title}\n  {published}\n  {link}\n  {summary}\n\n"

        # Ajout du texte à la page
        page.insert_text((72, 72), text, fontsize=11)

# Sauvegarde du PDF
pdf_doc.save(pdf_output)
pdf_doc.close()

# Sauvegarde du fichier de log
with open(log_output, "w", encoding="utf-8") as log_file:
    log_file.write(f"RSS Debug Log - {datetime.now().isoformat()}\n\n")
    log_file.write("\n".join(log_lines))

print(f"✅ PDF généré : {pdf_output}")
print(f"🪵 Log généré : {log_output}")
