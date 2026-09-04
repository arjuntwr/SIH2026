import urllib.request
import re

url = 'https://revenuedepartment.gujarat.gov.in/showpage.aspx?contentid=19'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        print("Circulars page bytes:", len(html))
        # Find PDF links
        matches = re.findall(r'href="([^"]+\.pdf)"[^>]*>([\s\S]*?)</a>', html, re.IGNORECASE)
        print("PDF links found:", len(matches))
        for href, title in matches[:10]:
            clean_title = re.sub(r'<[^>]+>', '', title).strip()
            print(f"  * {clean_title} -> {href}")
        # Find table rows
        rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', html)
        print("Table rows found:", len(rows))
        for r_item in rows[:5]:
            cells = re.findall(r'<td[^>]*>([\s\S]*?)</td>', r_item)
            if cells:
                clean_cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
                print("    Row:", clean_cells[:4])
except Exception as e:
    print("Err:", e)
