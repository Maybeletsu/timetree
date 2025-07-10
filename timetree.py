import requests
import datetime
import os

class TimeTreeClient:
    BASE = "https://timetreeapis.com"

    def __init__(self, token: str, calendar_id: str):
        self.token = token
        self.calendar_id = calendar_id
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}", "Accept": "application/vnd.timetree.v1+json"})

    def get_today_events(self):
        today = datetime.date.today().isoformat()
        url = f"{self.BASE}/calendars/{self.calendar_id}/events?include=creator"
        params = {"filter[since]": today, "filter[until]": today}
        r = self.session.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        events = []
        for e in data.get("data", []):
            attributes = e["attributes"]
            start = attributes["start_at"][:16].replace("T", " ")
            title = attributes["title"]
            category = attributes["category"]
            events.append({"start": start, "title": title, "category": category})
        return events
