import urllib.request
import re

url = 'https://revenuedepartment.gujarat.gov.in'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        # Extract menu items / circular links
        matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)</a>', html)
        print(f"Total links on Gujarat Revenue Dept: {len(matches)}")
        for href, text in matches:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            if any(w in clean_text.lower() for w in ['circular', 'act', 'rule', 'jantri', 'order', 'paripatra', 'revenue', 'resolution', 'na']):
                print(f"  * {clean_text} -> {href}")
except Exception as e:
    print("Err:", e)
