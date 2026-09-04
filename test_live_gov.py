import urllib.request
import re
import json

def test_indiacode():
    url = 'https://www.indiacode.nic.in/handle/123456789/2242'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'href="(/handle/123456789/\d+)">([^<]+)</a>', html)
            print("India Code Matches found:", len(matches))
            for m in matches[:6]:
                print("  Act:", m[1].strip(), "URL: https://www.indiacode.nic.in" + m[0])
    except Exception as e:
        print("India Code Error:", e)

def test_revenue_dept():
    url = 'https://revenuedepartment.gujarat.gov.in/ActsRules'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print("Gujarat Revenue Dept ActsRules length:", len(html))
            links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)
            print("Links found:", len(links))
            for l in links[:10]:
                if any(k in l[1].lower() for k in ['act', 'code', 'rule', 'revenue', 'circular', 'order']):
                    print("  GR/Act link:", l[1].strip(), "->", l[0])
    except Exception as e:
        print("Revenue Dept Error:", e)

if __name__ == '__main__':
    print("Testing India Code...")
    test_indiacode()
    print("\nTesting Gujarat Revenue Dept...")
    test_revenue_dept()
