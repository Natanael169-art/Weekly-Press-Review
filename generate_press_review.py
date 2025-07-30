# Revised script to generate a press review PDF and log file from individual RSS feeds per company

import csv
import fitz  # PyMuPDF
from datetime import datetime
import xml.etree.ElementTree as ET

# Load RSS feed URLs from CSV
rss_data = {}
with open("client_rss_feeds_cleaned.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        company = row.get("Company Name", "Unnamed Company")
        url = row.get("RSS Feed URL")
        if url:
            rss_data.setdefault(company, []).append(url)

# Prepare PDF document and log file
pdf_doc = fitz.open()
log_lines = []

# Process each company's feeds
for company, urls in rss_data.items():
    articles = []
    for url in urls:
        try:
            tree = ET.parse(url)
            root = tree.getroot()
            items = root.findall(".//item")
            if not items:
                log_lines.append(f"[EMPTY] {company} - No articles found in: {url}")
                continue
            for item in items:
                title = item.findtext("title", "No title")
                link = item.findtext("link", "")
                summary = item.findtext("description", "")
                pub_date = item.findtext("pubDate", "")
                articles.append(f"• {title}\n{pub_date}\n{link}\n{summary}\n")
        except Exception as e:
            log_lines.append(f"[ERROR] {company} - Exception: {str(e)}")

    # Add section to PDF
    page = pdf_doc.new_page()
    text = f"=== {company} ===\n\n"
    if articles:
        text += "\n\n".join(articles)
        log_lines.append(f"[OK] {company} - {len(articles)} articles retrieved.")
    else:
        text += "No articles available."
        log_lines.append(f"[EMPTY] {company} - No articles to display.")
    page.insert_text((72, 72), text, fontsize=11)

# Save PDF and log file
pdf_doc.save("weekly_press_review.pdf")
with open("rss_debug_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write("\n".join(log_lines))

print("PDF and log file generated successfully.")