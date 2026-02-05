#!/usr/bin/env python3
"""
Download vehicle icons from Twemoji (Twitter's open source emoji)
These are high quality, consistent PNG images
"""

import os
import urllib.request
import ssl
import time
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

ssl._create_default_https_context = ssl._create_unverified_context

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(BASE_DIR, 'images', 'vehicles')
os.makedirs(SAVE_DIR, exist_ok=True)

# Twemoji CDN: https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets/72x72/{code}.png
# Code is the emoji's Unicode codepoint in lowercase hex

# Mapping: filename -> (twemoji_code, english_name, chinese_name)
# These are all verified to exist in Twemoji
TWEMOJI_VEHICLES = {
    # === Emoji-based vehicles with Twemoji codes ===
    # Cars & Ground vehicles
    'car.png': ('1f697', 'Car', '汽车'),
    'red-car.png': ('1f697', 'Red Car', '红色汽车'),
    'taxi.png': ('1f695', 'Taxi', '出租车'),
    'suv.png': ('1f699', 'SUV', '越野车'),
    'pickup-truck.png': ('1f6fb', 'Pickup Truck', '皮卡车'),
    'delivery-truck.png': ('1f69a', 'Delivery Truck', '送货车'),
    'articulated-truck.png': ('1f69b', 'Semi Truck', '半挂车'),
    'racing-car.png': ('1f3ce', 'Racing Car', '赛车'),
    'sports-car.png': ('1f3ce', 'Sports Car', '跑车'),

    # Buses
    'bus.png': ('1f68c', 'Bus', '公交车'),
    'trolleybus.png': ('1f68e', 'Trolleybus', '无轨电车'),
    'minibus.png': ('1f690', 'Minibus', '小巴'),

    # Emergency vehicles
    'ambulance.png': ('1f691', 'Ambulance', '救护车'),
    'fire-engine.png': ('1f692', 'Fire Engine', '消防车'),
    'police-car.png': ('1f693', 'Police Car', '警车'),

    # Two-wheelers
    'motorcycle.png': ('1f3cd', 'Motorcycle', '摩托车'),
    'motor-scooter.png': ('1f6f5', 'Scooter', '踏板车'),
    'bicycle.png': ('1f6b2', 'Bicycle', '自行车'),
    'kick-scooter.png': ('1f6f4', 'Kick Scooter', '滑板车'),

    # Other land vehicles
    'tractor.png': ('1f69c', 'Tractor', '拖拉机'),
    'rickshaw.png': ('1f6fa', 'Auto Rickshaw', '三轮车'),
    'skateboard.png': ('1f6f9', 'Skateboard', '滑板'),
    'roller-skate.png': ('1f6fc', 'Roller Skate', '轮滑鞋'),
    'sled.png': ('1f6f7', 'Sled', '雪橇'),
    'wheelchair.png': ('1f9bd', 'Wheelchair', '轮椅'),
    'motorized-wheelchair.png': ('1f9bc', 'Motorized Wheelchair', '电动轮椅'),

    # Rail vehicles
    'train.png': ('1f682', 'Locomotive', '火车'),
    'steam-train.png': ('1f682', 'Steam Train', '蒸汽火车'),
    'high-speed-train.png': ('1f684', 'High Speed Train', '高铁'),
    'bullet-train.png': ('1f685', 'Bullet Train', '子弹头列车'),
    'metro.png': ('1f687', 'Metro', '地铁'),
    'tram.png': ('1f68a', 'Tram', '有轨电车'),
    'monorail.png': ('1f69d', 'Monorail', '单轨'),
    'light-rail.png': ('1f688', 'Light Rail', '轻轨'),
    'train-car.png': ('1f683', 'Train Car', '车厢'),
    'cable-car.png': ('1f6a1', 'Cable Car', '缆车'),
    'gondola.png': ('1f6a0', 'Gondola', '吊舱'),
    'funicular.png': ('1f69e', 'Funicular', '登山缆车'),

    # Aircraft
    'airplane.png': ('2708', 'Airplane', '飞机'),
    'small-airplane.png': ('1f6e9', 'Small Airplane', '小型飞机'),
    'helicopter.png': ('1f681', 'Helicopter', '直升机'),
    'rocket.png': ('1f680', 'Rocket', '火箭'),
    'flying-saucer.png': ('1f6f8', 'UFO', '飞碟'),
    'parachute.png': ('1fa82', 'Parachute', '降落伞'),

    # Watercraft
    'sailboat.png': ('26f5', 'Sailboat', '帆船'),
    'speedboat.png': ('1f6a4', 'Speedboat', '快艇'),
    'passenger-ship.png': ('1f6f3', 'Cruise Ship', '游轮'),
    'ferry.png': ('26f4', 'Ferry', '渡轮'),
    'ship.png': ('1f6a2', 'Ship', '轮船'),
    'canoe.png': ('1f6f6', 'Canoe', '独木舟'),

    # Special
    'hot-air-balloon.png': ('1f388', 'Balloon', '气球'),
}


def download_twemoji(filename, code, english, chinese):
    """Download a single Twemoji PNG"""
    filepath = os.path.join(SAVE_DIR, filename)

    if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
        return True, 'exists'

    # Twemoji CDN URL
    url = f'https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets/72x72/{code}.png'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()

        if len(data) < 500:
            return False, 'too small'

        # Verify PNG signature
        if not data.startswith(b'\x89PNG'):
            return False, 'not PNG'

        with open(filepath, 'wb') as f:
            f.write(data)

        return True, 'OK'

    except Exception as e:
        return False, str(e)[:30]


def generate_verification_html():
    """Generate HTML verification page"""
    html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Twemoji Vehicle Icons - Verification</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f0f4f8; }
        h1 { text-align: center; color: #333; }
        .info { text-align: center; background: white; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }
        .card { background: white; border-radius: 12px; padding: 12px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .card img { width: 72px; height: 72px; margin-bottom: 8px; }
        .card .en { font-size: 13px; font-weight: bold; color: #333; }
        .card .zh { font-size: 12px; color: #666; margin-top: 4px; }
        .card.missing { background: #ffe0e0; }
        .card.ok { border: 2px solid #4CAF50; }
    </style>
</head>
<body>
    <h1>Twemoji Vehicle Icons</h1>
    <div class="info">
        <p><strong>Instructions:</strong> Check each icon matches its label.</p>
        <p>Green border = downloaded successfully | Red background = missing</p>
    </div>
    <div class="grid">
'''

    for filename, (code, english, chinese) in TWEMOJI_VEHICLES.items():
        filepath = os.path.join(SAVE_DIR, filename)
        exists = os.path.exists(filepath) and os.path.getsize(filepath) > 500

        card_class = 'ok' if exists else 'missing'
        img_tag = f'<img src="images/vehicles/{filename}" alt="{english}">' if exists else '<div style="width:72px;height:72px;background:#eee;margin:0 auto 8px;border-radius:10px;line-height:72px;">?</div>'

        html += f'''
        <div class="card {card_class}">
            {img_tag}
            <div class="en">{english}</div>
            <div class="zh">{chinese}</div>
        </div>
'''

    html += '''
    </div>
</body>
</html>
'''

    path = os.path.join(BASE_DIR, 'verify-twemoji.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    return path


def main():
    print('=' * 50)
    print('Twemoji Vehicle Icons Downloader')
    print('=' * 50)
    print(f'\nSave to: {SAVE_DIR}')
    print(f'Total icons: {len(TWEMOJI_VEHICLES)}')
    print('\nDownloading...\n')

    success = 0
    fail = 0

    for filename, (code, english, chinese) in TWEMOJI_VEHICLES.items():
        ok, status = download_twemoji(filename, code, english, chinese)
        if ok:
            success += 1
            print(f'  [OK] {filename}')
        else:
            fail += 1
            print(f'  [FAIL] {filename}: {status}')
        time.sleep(0.15)

    print('\n' + '=' * 50)
    print(f'Done! Success: {success}, Failed: {fail}')

    verify = generate_verification_html()
    print(f'\nVerification page: {verify}')
    print('Open in browser to check icons!')
    print('=' * 50)


if __name__ == '__main__':
    main()
