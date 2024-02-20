# populate_db.py
import os
import json
import django
from datetime import datetime, timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

from dashboard_app.models import Insight

def populate_database():
    with open('jsondata.json', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        # Parse datetime strings and convert them to aware datetime objects
        added = datetime.strptime(item.get('added', ''), "%B, %d %Y %H:%M:%S")
        added = added.replace(tzinfo=timezone.utc)  # Assuming datetime strings are in UTC

        published_str = item.get('published', '')
        published = datetime.strptime(published_str, "%B, %d %Y %H:%M:%S") if published_str else None
        published = published.replace(tzinfo=timezone.utc) if published else None

        # Handle empty or missing values for each column
        end_year = item.get('end_year') or None
        intensity = item.get('intensity') or None
        sector = item.get('sector') or None
        topic = item.get('topic') or None
        insight = item.get('insight') or None
        url = item.get('url') or None
        region = item.get('region') or None
        start_year = item.get('start_year') or None
        impact = item.get('impact') or None
        country = item.get('country') or None
        relevance = item.get('relevance') or None
        pestle = item.get('pestle') or None
        source = item.get('source') or None
        title = item.get('title') or None
        likelihood = item.get('likelihood') or None

        # Create Insight objects and save them to the database
        Insight.objects.create(
            end_year=end_year,
            intensity=intensity,
            sector=sector,
            topic=topic,
            insight=insight,
            url=url,
            region=region,
            start_year=start_year,
            impact=impact,
            added=added,
            published=published,
            country=country,
            relevance=relevance,
            pestle=pestle,
            source=source,
            title=title,
            likelihood=likelihood
        )

if __name__ == '__main__':
    populate_database()
