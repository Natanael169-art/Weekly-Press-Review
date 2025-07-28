import pandas as pd
import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime
import time
import html
import urllib.parse

# Charger le fichier CSV
df = pd.read_csv("client_rss_feeds.csv")

# Nettoyer et corriger les URLs
df = df[['Company', 'RSS Feed URL']].dropna()
df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: html.unescape(str(x)).strip())
df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: x if x.startswith('http') else 'https://news.google.com' + x)
df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: urllib.parse.quote(x, safe=':/?&=+'))

# Collecter les articles
all_entries = []
for _, row in df.iterrows():
    company = row['Company']
    url = row['RSS Feed URL']
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            entry.source_title = company
            all_entries.append(entry)
    except Exception as e:
        print(f"Erreur pour {company} : {e}")

# Trier par date
def get_published(entry):
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        return datetime.fromtimestamp(time.mktime(entry.published_parsed))
    return datetime.min

all_entries.sort(key=get_published, reverse=True)

# Générer le flux RSS combiné
fg = FeedGenerator()
fg.title('Flux RSS combiné')
fg.link(href='https://example.com/combined-feed', rel='self')
fg.description('Ce flux regroupe plusieurs sources RSS triées par date.')

for entry in all_entries:
    fe = fg.add_entry()
    fe.title(entry.title)
    fe.link(href=entry.link)
    fe.description(entry.get('summary', ''))
    fe.pubDate(entry.get('published', ''))
    fe.source({'url': entry.link, 'title': entry.source_title})

# Sauvegarder le fichier
fg.rss_file('flux_rss_combine.xml')
