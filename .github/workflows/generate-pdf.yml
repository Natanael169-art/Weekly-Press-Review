{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "{"
                },
                {
                    "line_number": 2,
                    "text": "\"chunks\": ["
                },
                {
                    "line_number": 3,
                    "text": "{"
                },
                {
                    "line_number": 4,
                    "text": "\"type\": \"txt\","
                },
                {
                    "line_number": 5,
                    "text": "\"chunk_number\": 1,"
                },
                {
                    "line_number": 6,
                    "text": "\"lines\": ["
                },
                {
                    "line_number": 7,
                    "text": "{"
                },
                {
                    "line_number": 8,
                    "text": "\"line_number\": 1,"
                },
                {
                    "line_number": 9,
                    "text": "\"text\": \"import pandas as pd\""
                },
                {
                    "line_number": 10,
                    "text": "},"
                },
                {
                    "line_number": 11,
                    "text": "{"
                },
                {
                    "line_number": 12,
                    "text": "\"line_number\": 2,"
                },
                {
                    "line_number": 13,
                    "text": "\"text\": \"import feedparser\""
                },
                {
                    "line_number": 14,
                    "text": "},"
                },
                {
                    "line_number": 15,
                    "text": "{"
                },
                {
                    "line_number": 16,
                    "text": "\"line_number\": 3,"
                },
                {
                    "line_number": 17,
                    "text": "\"text\": \"from feedgen.feed import FeedGenerator\""
                },
                {
                    "line_number": 18,
                    "text": "},"
                },
                {
                    "line_number": 19,
                    "text": "{"
                },
                {
                    "line_number": 20,
                    "text": "\"line_number\": 4,"
                },
                {
                    "line_number": 21,
                    "text": "\"text\": \"from datetime import datetime\""
                },
                {
                    "line_number": 22,
                    "text": "},"
                },
                {
                    "line_number": 23,
                    "text": "{"
                },
                {
                    "line_number": 24,
                    "text": "\"line_number\": 5,"
                },
                {
                    "line_number": 25,
                    "text": "\"text\": \"import time\""
                },
                {
                    "line_number": 26,
                    "text": "},"
                },
                {
                    "line_number": 27,
                    "text": "{"
                },
                {
                    "line_number": 28,
                    "text": "\"line_number\": 6,"
                },
                {
                    "line_number": 29,
                    "text": "\"text\": \"import html\""
                },
                {
                    "line_number": 30,
                    "text": "},"
                },
                {
                    "line_number": 31,
                    "text": "{"
                },
                {
                    "line_number": 32,
                    "text": "\"line_number\": 7,"
                },
                {
                    "line_number": 33,
                    "text": "\"text\": \"import urllib.parse\""
                },
                {
                    "line_number": 34,
                    "text": "},"
                },
                {
                    "line_number": 35,
                    "text": "{"
                },
                {
                    "line_number": 36,
                    "text": "\"line_number\": 8,"
                },
                {
                    "line_number": 37,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 38,
                    "text": "},"
                },
                {
                    "line_number": 39,
                    "text": "{"
                },
                {
                    "line_number": 40,
                    "text": "\"line_number\": 9,"
                },
                {
                    "line_number": 41,
                    "text": "\"text\": \"# Charger le fichier CSV\""
                },
                {
                    "line_number": 42,
                    "text": "},"
                },
                {
                    "line_number": 43,
                    "text": "{"
                },
                {
                    "line_number": 44,
                    "text": "\"line_number\": 10,"
                },
                {
                    "line_number": 45,
                    "text": "\"text\": \"df = pd.read_csv(\\\"client_rss_feeds.csv\\\")\""
                },
                {
                    "line_number": 46,
                    "text": "},"
                },
                {
                    "line_number": 47,
                    "text": "{"
                },
                {
                    "line_number": 48,
                    "text": "\"line_number\": 11,"
                },
                {
                    "line_number": 49,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 50,
                    "text": "},"
                },
                {
                    "line_number": 51,
                    "text": "{"
                },
                {
                    "line_number": 52,
                    "text": "\"line_number\": 12,"
                },
                {
                    "line_number": 53,
                    "text": "\"text\": \"# Nettoyer et corriger les URLs\""
                },
                {
                    "line_number": 54,
                    "text": "},"
                },
                {
                    "line_number": 55,
                    "text": "{"
                },
                {
                    "line_number": 56,
                    "text": "\"line_number\": 13,"
                },
                {
                    "line_number": 57,
                    "text": "\"text\": \"df = df[['Company', 'RSS Feed URL']].dropna()\""
                },
                {
                    "line_number": 58,
                    "text": "},"
                },
                {
                    "line_number": 59,
                    "text": "{"
                },
                {
                    "line_number": 60,
                    "text": "\"line_number\": 14,"
                },
                {
                    "line_number": 61,
                    "text": "\"text\": \"df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: html.unescape(str(x)).strip())\""
                },
                {
                    "line_number": 62,
                    "text": "},"
                },
                {
                    "line_number": 63,
                    "text": "{"
                },
                {
                    "line_number": 64,
                    "text": "\"line_number\": 15,"
                },
                {
                    "line_number": 65,
                    "text": "\"text\": \"df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: x if x.startswith('http') else 'https://news.google.com' + x)\""
                },
                {
                    "line_number": 66,
                    "text": "},"
                },
                {
                    "line_number": 67,
                    "text": "{"
                },
                {
                    "line_number": 68,
                    "text": "\"line_number\": 16,"
                },
                {
                    "line_number": 69,
                    "text": "\"text\": \"df['RSS Feed URL'] = df['RSS Feed URL'].apply(lambda x: urllib.parse.quote(x, safe=':/?&=+'))\""
                },
                {
                    "line_number": 70,
                    "text": "},"
                },
                {
                    "line_number": 71,
                    "text": "{"
                },
                {
                    "line_number": 72,
                    "text": "\"line_number\": 17,"
                },
                {
                    "line_number": 73,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 74,
                    "text": "},"
                },
                {
                    "line_number": 75,
                    "text": "{"
                },
                {
                    "line_number": 76,
                    "text": "\"line_number\": 18,"
                },
                {
                    "line_number": 77,
                    "text": "\"text\": \"# Collecter les articles\""
                },
                {
                    "line_number": 78,
                    "text": "},"
                },
                {
                    "line_number": 79,
                    "text": "{"
                },
                {
                    "line_number": 80,
                    "text": "\"line_number\": 19,"
                },
                {
                    "line_number": 81,
                    "text": "\"text\": \"all_entries = []\""
                },
                {
                    "line_number": 82,
                    "text": "},"
                },
                {
                    "line_number": 83,
                    "text": "{"
                },
                {
                    "line_number": 84,
                    "text": "\"line_number\": 20,"
                },
                {
                    "line_number": 85,
                    "text": "\"text\": \"for _, row in df.iterrows():\""
                },
                {
                    "line_number": 86,
                    "text": "},"
                },
                {
                    "line_number": 87,
                    "text": "{"
                },
                {
                    "line_number": 88,
                    "text": "\"line_number\": 21,"
                },
                {
                    "line_number": 89,
                    "text": "\"text\": \"company = row['Company']\""
                },
                {
                    "line_number": 90,
                    "text": "},"
                },
                {
                    "line_number": 91,
                    "text": "{"
                },
                {
                    "line_number": 92,
                    "text": "\"line_number\": 22,"
                },
                {
                    "line_number": 93,
                    "text": "\"text\": \"url = row['RSS Feed URL']\""
                },
                {
                    "line_number": 94,
                    "text": "},"
                },
                {
                    "line_number": 95,
                    "text": "{"
                },
                {
                    "line_number": 96,
                    "text": "\"line_number\": 23,"
                },
                {
                    "line_number": 97,
                    "text": "\"text\": \"try:\""
                },
                {
                    "line_number": 98,
                    "text": "},"
                },
                {
                    "line_number": 99,
                    "text": "{"
                },
                {
                    "line_number": 100,
                    "text": "\"line_number\": 24,"
                },
                {
                    "line_number": 101,
                    "text": "\"text\": \"feed = feedparser.parse(url)\""
                },
                {
                    "line_number": 102,
                    "text": "},"
                },
                {
                    "line_number": 103,
                    "text": "{"
                },
                {
                    "line_number": 104,
                    "text": "\"line_number\": 25,"
                },
                {
                    "line_number": 105,
                    "text": "\"text\": \"for entry in feed.entries:\""
                },
                {
                    "line_number": 106,
                    "text": "},"
                },
                {
                    "line_number": 107,
                    "text": "{"
                },
                {
                    "line_number": 108,
                    "text": "\"line_number\": 26,"
                },
                {
                    "line_number": 109,
                    "text": "\"text\": \"entry.source_title = company\""
                },
                {
                    "line_number": 110,
                    "text": "},"
                },
                {
                    "line_number": 111,
                    "text": "{"
                },
                {
                    "line_number": 112,
                    "text": "\"line_number\": 27,"
                },
                {
                    "line_number": 113,
                    "text": "\"text\": \"all_entries.append(entry)\""
                },
                {
                    "line_number": 114,
                    "text": "},"
                },
                {
                    "line_number": 115,
                    "text": "{"
                },
                {
                    "line_number": 116,
                    "text": "\"line_number\": 28,"
                },
                {
                    "line_number": 117,
                    "text": "\"text\": \"except Exception as e:\""
                },
                {
                    "line_number": 118,
                    "text": "},"
                },
                {
                    "line_number": 119,
                    "text": "{"
                },
                {
                    "line_number": 120,
                    "text": "\"line_number\": 29,"
                },
                {
                    "line_number": 121,
                    "text": "\"text\": \"print(f\\\"Erreur pour {company} : {e}\\\")\""
                },
                {
                    "line_number": 122,
                    "text": "},"
                },
                {
                    "line_number": 123,
                    "text": "{"
                },
                {
                    "line_number": 124,
                    "text": "\"line_number\": 30,"
                },
                {
                    "line_number": 125,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 126,
                    "text": "},"
                },
                {
                    "line_number": 127,
                    "text": "{"
                },
                {
                    "line_number": 128,
                    "text": "\"line_number\": 31,"
                },
                {
                    "line_number": 129,
                    "text": "\"text\": \"# Trier par date\""
                },
                {
                    "line_number": 130,
                    "text": "},"
                },
                {
                    "line_number": 131,
                    "text": "{"
                },
                {
                    "line_number": 132,
                    "text": "\"line_number\": 32,"
                },
                {
                    "line_number": 133,
                    "text": "\"text\": \"def get_published(entry):\""
                },
                {
                    "line_number": 134,
                    "text": "},"
                },
                {
                    "line_number": 135,
                    "text": "{"
                },
                {
                    "line_number": 136,
                    "text": "\"line_number\": 33,"
                },
                {
                    "line_number": 137,
                    "text": "\"text\": \"if hasattr(entry, 'published_parsed') and entry.published_parsed:\""
                },
                {
                    "line_number": 138,
                    "text": "},"
                },
                {
                    "line_number": 139,
                    "text": "{"
                },
                {
                    "line_number": 140,
                    "text": "\"line_number\": 34,"
                },
                {
                    "line_number": 141,
                    "text": "\"text\": \"return datetime.fromtimestamp(time.mktime(entry.published_parsed))\""
                },
                {
                    "line_number": 142,
                    "text": "},"
                },
                {
                    "line_number": 143,
                    "text": "{"
                },
                {
                    "line_number": 144,
                    "text": "\"line_number\": 35,"
                },
                {
                    "line_number": 145,
                    "text": "\"text\": \"return datetime.min\""
                },
                {
                    "line_number": 146,
                    "text": "},"
                },
                {
                    "line_number": 147,
                    "text": "{"
                },
                {
                    "line_number": 148,
                    "text": "\"line_number\": 36,"
                },
                {
                    "line_number": 149,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 150,
                    "text": "},"
                },
                {
                    "line_number": 151,
                    "text": "{"
                },
                {
                    "line_number": 152,
                    "text": "\"line_number\": 37,"
                },
                {
                    "line_number": 153,
                    "text": "\"text\": \"all_entries.sort(key=get_published, reverse=True)\""
                },
                {
                    "line_number": 154,
                    "text": "},"
                },
                {
                    "line_number": 155,
                    "text": "{"
                },
                {
                    "line_number": 156,
                    "text": "\"line_number\": 38,"
                },
                {
                    "line_number": 157,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 158,
                    "text": "},"
                },
                {
                    "line_number": 159,
                    "text": "{"
                },
                {
                    "line_number": 160,
                    "text": "\"line_number\": 39,"
                },
                {
                    "line_number": 161,
                    "text": "\"text\": \"# G\\u00e9n\\u00e9rer le flux RSS combin\\u00e9\""
                },
                {
                    "line_number": 162,
                    "text": "},"
                },
                {
                    "line_number": 163,
                    "text": "{"
                },
                {
                    "line_number": 164,
                    "text": "\"line_number\": 40,"
                },
                {
                    "line_number": 165,
                    "text": "\"text\": \"fg = FeedGenerator()\""
                },
                {
                    "line_number": 166,
                    "text": "},"
                },
                {
                    "line_number": 167,
                    "text": "{"
                },
                {
                    "line_number": 168,
                    "text": "\"line_number\": 41,"
                },
                {
                    "line_number": 169,
                    "text": "\"text\": \"fg.title('Flux RSS combin\\u00e9')\""
                },
                {
                    "line_number": 170,
                    "text": "},"
                },
                {
                    "line_number": 171,
                    "text": "{"
                },
                {
                    "line_number": 172,
                    "text": "\"line_number\": 42,"
                },
                {
                    "line_number": 173,
                    "text": "\"text\": \"fg.link(href='https://example.com/combined-feed', rel='self')\""
                },
                {
                    "line_number": 174,
                    "text": "},"
                },
                {
                    "line_number": 175,
                    "text": "{"
                },
                {
                    "line_number": 176,
                    "text": "\"line_number\": 43,"
                },
                {
                    "line_number": 177,
                    "text": "\"text\": \"fg.description('Ce flux regroupe plusieurs sources RSS tri\\u00e9es par date.')\""
                },
                {
                    "line_number": 178,
                    "text": "},"
                },
                {
                    "line_number": 179,
                    "text": "{"
                },
                {
                    "line_number": 180,
                    "text": "\"line_number\": 44,"
                },
                {
                    "line_number": 181,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 182,
                    "text": "},"
                },
                {
                    "line_number": 183,
                    "text": "{"
                },
                {
                    "line_number": 184,
                    "text": "\"line_number\": 45,"
                },
                {
                    "line_number": 185,
                    "text": "\"text\": \"for entry in all_entries:\""
                },
                {
                    "line_number": 186,
                    "text": "},"
                },
                {
                    "line_number": 187,
                    "text": "{"
                },
                {
                    "line_number": 188,
                    "text": "\"line_number\": 46,"
                },
                {
                    "line_number": 189,
                    "text": "\"text\": \"fe = fg.add_entry()\""
                },
                {
                    "line_number": 190,
                    "text": "},"
                },
                {
                    "line_number": 191,
                    "text": "{"
                },
                {
                    "line_number": 192,
                    "text": "\"line_number\": 47,"
                },
                {
                    "line_number": 193,
                    "text": "\"text\": \"fe.title(entry.title)\""
                },
                {
                    "line_number": 194,
                    "text": "},"
                },
                {
                    "line_number": 195,
                    "text": "{"
                },
                {
                    "line_number": 196,
                    "text": "\"line_number\": 48,"
                },
                {
                    "line_number": 197,
                    "text": "\"text\": \"fe.link(href=entry.link)\""
                },
                {
                    "line_number": 198,
                    "text": "},"
                },
                {
                    "line_number": 199,
                    "text": "{"
                },
                {
                    "line_number": 200,
                    "text": "\"line_number\": 49,"
                },
                {
                    "line_number": 201,
                    "text": "\"text\": \"fe.description(entry.get('summary', ''))\""
                },
                {
                    "line_number": 202,
                    "text": "},"
                },
                {
                    "line_number": 203,
                    "text": "{"
                },
                {
                    "line_number": 204,
                    "text": "\"line_number\": 50,"
                },
                {
                    "line_number": 205,
                    "text": "\"text\": \"fe.pubDate(entry.get('published', ''))\""
                },
                {
                    "line_number": 206,
                    "text": "},"
                },
                {
                    "line_number": 207,
                    "text": "{"
                },
                {
                    "line_number": 208,
                    "text": "\"line_number\": 51,"
                },
                {
                    "line_number": 209,
                    "text": "\"text\": \"fe.source({'url': entry.link, 'title': entry.source_title})\""
                },
                {
                    "line_number": 210,
                    "text": "},"
                },
                {
                    "line_number": 211,
                    "text": "{"
                },
                {
                    "line_number": 212,
                    "text": "\"line_number\": 52,"
                },
                {
                    "line_number": 213,
                    "text": "\"text\": \"\""
                },
                {
                    "line_number": 214,
                    "text": "},"
                },
                {
                    "line_number": 215,
                    "text": "{"
                },
                {
                    "line_number": 216,
                    "text": "\"line_number\": 53,"
                },
                {
                    "line_number": 217,
                    "text": "\"text\": \"# Sauvegarder le fichier\""
                },
                {
                    "line_number": 218,
                    "text": "},"
                },
                {
                    "line_number": 219,
                    "text": "{"
                },
                {
                    "line_number": 220,
                    "text": "\"line_number\": 54,"
                },
                {
                    "line_number": 221,
                    "text": "\"text\": \"fg.rss_file('flux_rss_combine.xml')\""
                },
                {
                    "line_number": 222,
                    "text": "}"
                },
                {
                    "line_number": 223,
                    "text": "],"
                },
                {
                    "line_number": 224,
                    "text": "\"token_count\": 192"
                },
                {
                    "line_number": 225,
                    "text": "}"
                },
                {
                    "line_number": 226,
                    "text": "]"
                },
                {
                    "line_number": 227,
                    "text": "}"
                }
            ],
            "token_count": 3196
        }
    ]
}