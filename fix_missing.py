import os
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

SAVE_DIR = os.path.join(os.path.dirname(__file__), 'images', 'vehicles')

images = {
    'harvester.png': 'https://cdn-icons-png.flaticon.com/128/2138/2138440.png',
    'tank.png': 'https://cdn-icons-png.flaticon.com/128/1085/1085803.png',
}

for filename, url in images.items():
    filepath = os.path.join(SAVE_DIR, filename)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'image/png,image/*,*/*;q=0.8',
            'Referer': 'https://www.flaticon.com/'
        }
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
        with open(filepath, 'wb') as f:
            f.write(data)
        print(f'[OK] {filename}')
    except Exception as e:
        print(f'[FAIL] {filename}: {e}')
