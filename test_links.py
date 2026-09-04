import urllib.request
import re

url = 'https://www.indiacode.nic.in'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        print("Length of homepage:", len(html))
        # Look for state enactments link
        for line in html.splitlines():
            if 'gujarat' in line.lower() or 'state-acts' in line.lower() or 'handle/' in line.lower():
                print("  Line:", line.strip()[:140])
except Exception as e:
    print("Err:", e)
