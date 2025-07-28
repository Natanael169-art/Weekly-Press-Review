import feedparser
import csv
import xml.etree.ElementTree as ET
from datetime import datetime

# Lire les URLs RSS depuis le fichier CSV
rss_urls = []
with open("client_rss_feeds_cleaned.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row.get("RSS Feed URL")
        if url:
            rss_urls.append(url)

# Créer la structure du flux RSS combiné
rss_root = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss_root, "channel")
ET.SubElement(channel, "title").text = "Combined RSS Feed"
ET.SubElement(channel, "link").text = "https://example.com"
ET.SubElement(channel, "description").text = "Aggregated news from client companies"
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

# Ajouter les articles de chaque flux
for url in rss_urls:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = entry.get("title", "No title")
        ET.SubElement(item, "link").text = entry.get("link", "")
        ET.SubElement(item, "description").text = entry.get("summary", "")
        pub_date = entry.get("published", "") or entry.get("updated", "")
        ET.SubElement(item, "pubDate").text = pub_date

# Sauvegarder dans flux.xml
tree = ET.ElementTree(rss_root)
tree.write("flux.xml", encoding="utf-8", xml_declaration=True)

print("flux.xml has been generated successfully.")
