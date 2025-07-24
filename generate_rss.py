import csv
import feedparser
import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

# Charger les flux RSS depuis le fichier CSV
rss_urls = []
with open("client_rss_feeds_cleaned.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row.get("RSS Feed URL")
        if url:
            rss_urls.append(url.strip('"'))

# Définir la période de 7 jours
now = datetime.datetime.utcnow()
seven_days_ago = now - datetime.timedelta(days=7)

# Collecter les articles récents
entries = []
for url in rss_urls:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if hasattr(entry, 'published_parsed'):
            published = datetime.datetime(*entry.published_parsed[:6])
            if published > seven_days_ago:
                entries.append({
                    'title': entry.title,
                    'link': entry.link,
                    'description': entry.get('summary', ''),
                    'pubDate': published.strftime('%a, %d %b %Y %H:%M:%S GMT')
                })

# Trier les articles par date décroissante
entries.sort(key=lambda x: x['pubDate'], reverse=True)

# Générer le fichier RSS
rss = Element('rss', version='2.0')
channel = SubElement(rss, 'channel')
SubElement(channel, 'title').text = 'Weekly Press Review'
SubElement(channel, 'link').text = 'https://natanael169-art.github.io/Weekly-Press-Review/rss.xml'
SubElement(channel, 'description').text = 'A weekly summary of news articles from client companies.'
SubElement(channel, 'language').text = 'en-us'
SubElement(channel, 'lastBuildDate').text = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

for entry in entries:
    item = SubElement(channel, 'item')
    SubElement(item, 'title').text = entry['title']
    SubElement(item, 'link').text = entry['link']
    SubElement(item, 'description').text = entry['description']
    SubElement(item, 'pubDate').text = entry['pubDate']

tree = ElementTree(rss)
tree.write("rss.xml", encoding="utf-8", xml_declaration=True)
