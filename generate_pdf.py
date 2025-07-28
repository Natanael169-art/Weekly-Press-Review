{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "import pandas as pd"
                },
                {
                    "line_number": 2,
                    "text": "import feedparser"
                },
                {
                    "line_number": 3,
                    "text": "from feedgen.feed import FeedGenerator"
                },
                {
                    "line_number": 4,
                    "text": "from datetime import datetime"
                },
                {
                    "line_number": 5,
                    "text": "import time"
                },
                {
                    "line_number": 6,
                    "text": "import html"
                },
                {
                    "line_number": 7,
                    "text": "import urllib.parse"
                },
                {
                    "line_number": 8,
                    "text": ""
                },
                {
                    "line_number": 9,
                    "text": "# Charger le fichier CSV"
                },
                {
                    "line_number": 10,
                    "text": "df = pd.read_csv(\"client_rss_feeds.csv\")"
                },
                {
                    "line_number": 11,
                    "text": ""
                },
                {
                    "line_number": 12,
                    "text": "# Nettoyer et corriger les URLs"
                },
                {
                    "line_number": 13,
                    "text": "df = df[['Company', 'RSS Feed URL']].dropna()"
                },
                {
                    "line_number": 14,
                    "text": "df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: html.unescape(str(x)).strip())"
                },
                {
                    "line_number": 15,
                    "text": "df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: x if x.startswith('http') else 'https://news.google.com' + x)"
                },
                {
                    "line_number": 16,
                    "text": "df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: urllib.parse.quote(x, safe=':/?&=+'))"
                },
                {
                    "line_number": 17,
                    "text": ""
                },
                {
                    "line_number": 18,
                    "text": "# Collecter les articles"
                },
                {
                    "line_number": 19,
                    "text": "all_entries = []"
                },
                {
                    "line_number": 20,
                    "text": "for _, row in df.iterrows():"
                },
                {
                    "line_number": 21,
                    "text": "company = row['Company']"
                },
                {
                    "line_number": 22,
                    "text": "url = row['RSS Feed URL']"
                },
                {
                    "line_number": 23,
                    "text": "try:"
                },
                {
                    "line_number": 24,
                    "text": "feed = feedparser.parse(url)"
                },
                {
                    "line_number": 25,
                    "text": "for entry in feed.entries:"
                },
                {
                    "line_number": 26,
                    "text": "entry.source_title = company"
                },
                {
                    "line_number": 27,
                    "text": "all_entries.append(entry)"
                },
                {
                    "line_number": 28,
                    "text": "except Exception as e:"
                },
                {
                    "line_number": 29,
                    "text": "print(f\"Erreur pour {company} : {e}\")"
                },
                {
                    "line_number": 30,
                    "text": ""
                },
                {
                    "line_number": 31,
                    "text": "# Trier par date"
                },
                {
                    "line_number": 32,
                    "text": "def get_published(entry):"
                },
                {
                    "line_number": 33,
                    "text": "if hasattr(entry, 'published_parsed') and entry.published_parsed:"
                },
                {
                    "line_number": 34,
                    "text": "return datetime.fromtimestamp(time.mktime(entry.published_parsed))"
                },
                {
                    "line_number": 35,
                    "text": "return datetime.min"
                },
                {
                    "line_number": 36,
                    "text": ""
                },
                {
                    "line_number": 37,
                    "text": "all_entries.sort(key=get_published, reverse=True)"
                },
                {
                    "line_number": 38,
                    "text": ""
                },
                {
                    "line_number": 39,
                    "text": "# G\u00e9n\u00e9rer le flux RSS combin\u00e9"
                },
                {
                    "line_number": 40,
                    "text": "fg = FeedGenerator()"
                },
                {
                    "line_number": 41,
                    "text": "fg.title('Flux RSS combin\u00e9')"
                },
                {
                    "line_number": 42,
                    "text": "fg.link(href='https://example.com/combined-feed', rel='self')"
                },
                {
                    "line_number": 43,
                    "text": "fg.description('Ce flux regroupe plusieurs sources RSS tri\u00e9es par date.')"
                },
                {
                    "line_number": 44,
                    "text": ""
                },
                {
                    "line_number": 45,
                    "text": "for entry in all_entries:"
                },
                {
                    "line_number": 46,
                    "text": "fe = fg.add_entry()"
                },
                {
                    "line_number": 47,
                    "text": "fe.title(entry.title)"
                },
                {
                    "line_number": 48,
                    "text": "fe.link(href=entry.link)"
                },
                {
                    "line_number": 49,
                    "text": "fe.description(entry.get('summary', ''))"
                },
                {
                    "line_number": 50,
                    "text": "fe.pubDate(entry.get('published', ''))"
                },
                {
                    "line_number": 51,
                    "text": "fe.source({'url': entry.link, 'title': entry.source_title})"
                },
                {
                    "line_number": 52,
                    "text": ""
                },
                {
                    "line_number": 53,
                    "text": "# Sauvegarder le fichier"
                },
                {
                    "line_number": 54,
                    "text": "fg.rss_file('flux_rss_combine.xml')"
                }
            ],
            "token_count": 192
        }
    ]
}