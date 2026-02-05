#!/usr/bin/env python3
"""
Vehicle Icon Download Script
Uses Iconify API (free, reliable icon library)
Downloads SVG icons and generates a verification HTML page
"""

import os
import urllib.request
import ssl
import time
import sys
import json

# Fix Windows encoding
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(BASE_DIR, 'images', 'vehicles')
os.makedirs(SAVE_DIR, exist_ok=True)

# Iconify API base URL
# Format: https://api.iconify.design/{prefix}/{name}.svg
# Popular icon sets: noto (Google Noto Emoji), twemoji, fxemoji, openmoji

# Vehicle icons mapping: filename -> (icon_set, icon_name, chinese_name)
# Using multiple icon sets for best coverage
VEHICLE_ICONS = {
    # === Cars ===
    'suv.png': ('noto', 'sport-utility-vehicle', 'SUV越野车'),
    'sedan.png': ('noto', 'automobile', '轿车'),
    'convertible.png': ('fxemoji', 'convertible', '敞篷车'),
    'minivan.png': ('noto', 'minibus', '小型货车'),
    'electric-car.png': ('noto', 'automobile', '电动汽车'),
    'vintage-car.png': ('twemoji', 'automobile', '老爷车'),
    'limousine.png': ('fxemoji', 'limousine', '豪华轿车'),
    'jeep.png': ('noto', 'sport-utility-vehicle', '吉普车'),
    'hatchback.png': ('noto', 'automobile', '掀背车'),

    # === Trucks ===
    'moving-truck.png': ('noto', 'articulated-lorry', '搬家车'),
    'semi-truck.png': ('noto', 'articulated-lorry', '半挂车'),
    'tanker-truck.png': ('fxemoji', 'tankertruck', '油罐车'),
    'dump-truck.png': ('fxemoji', 'dumptruck', '自卸车'),
    'garbage-truck.png': ('fxemoji', 'garbagetruck', '垃圾车'),
    'ice-cream-truck.png': ('fxemoji', 'icecreamtruck', '冰淇淋车'),
    'food-truck.png': ('noto', 'delivery-truck', '餐车'),
    'tow-truck.png': ('fxemoji', 'towtruck', '拖车'),
    'flatbed-truck.png': ('noto', 'pickup-truck', '平板车'),
    'box-truck.png': ('noto', 'delivery-truck', '厢式货车'),
    'cement-mixer.png': ('fxemoji', 'cementmixer', '水泥搅拌车'),
    'logging-truck.png': ('noto', 'articulated-lorry', '运木车'),
    'cargo-truck.png': ('noto', 'delivery-truck', '货运卡车'),

    # === Public Transport ===
    'double-decker-bus.png': ('fxemoji', 'doubledeckerbus', '双层巴士'),
    'minibus.png': ('noto', 'minibus', '小巴'),
    'coach.png': ('noto', 'bus', '长途客车'),
    'shuttle-bus.png': ('noto', 'bus', '班车'),
    'airport-bus.png': ('noto', 'bus', '机场巴士'),
    'tour-bus.png': ('noto', 'bus', '旅游大巴'),
    'city-bus.png': ('noto', 'bus', '城市公交'),

    # === Taxis ===
    'black-cab.png': ('noto', 'taxi', '黑色出租车'),

    # === Emergency Vehicles ===
    'police-van.png': ('noto', 'police-car', '警用面包车'),
    'swat-truck.png': ('noto', 'police-car', '特警车'),
    'rescue-vehicle.png': ('noto', 'ambulance', '救援车'),
    'ladder-truck.png': ('noto', 'fire-engine', '云梯消防车'),
    'armored-car.png': ('noto', 'delivery-truck', '装甲车'),

    # === Construction Vehicles ===
    'excavator.png': ('fxemoji', 'excavator', '挖掘机'),
    'bulldozer.png': ('fxemoji', 'bulldozer', '推土机'),
    'crane.png': ('fxemoji', 'crane', '起重机'),
    'forklift.png': ('fxemoji', 'forklift', '叉车'),
    'roller.png': ('fxemoji', 'steamroller', '压路机'),
    'backhoe.png': ('fxemoji', 'excavator', '反铲挖掘机'),
    'loader.png': ('fxemoji', 'frontloader', '装载机'),
    'grader.png': ('fxemoji', 'grader', '平地机'),
    'paver.png': ('noto', 'delivery-truck', '铺路机'),
    'pile-driver.png': ('fxemoji', 'crane', '打桩机'),
    'concrete-pump.png': ('fxemoji', 'cementmixer', '混凝土泵车'),
    'tower-crane.png': ('fxemoji', 'towercrane', '塔吊'),
    'skid-steer.png': ('fxemoji', 'frontloader', '滑移装载机'),
    'compactor.png': ('fxemoji', 'steamroller', '压实机'),
    'asphalt-truck.png': ('noto', 'delivery-truck', '沥青车'),

    # === Farm Vehicles ===
    'harvester.png': ('fxemoji', 'harvester', '收割机'),
    'combine.png': ('fxemoji', 'harvester', '联合收割机'),
    'plow.png': ('noto', 'tractor', '犁车'),
    'seeder.png': ('noto', 'tractor', '播种机'),
    'sprayer.png': ('noto', 'tractor', '喷药车'),
    'baler.png': ('fxemoji', 'harvester', '打包机'),
    'farm-truck.png': ('noto', 'pickup-truck', '农用卡车'),
    'atv.png': ('noto', 'racing-motorcycle', '全地形车'),
    'utv.png': ('noto', 'sport-utility-vehicle', '多功能车'),

    # === Motorcycles ===
    'dirt-bike.png': ('noto', 'motorcycle', '越野摩托'),
    'chopper.png': ('noto', 'motorcycle', '哈雷摩托'),
    'sport-bike.png': ('noto', 'racing-motorcycle', '运动摩托'),
    'cruiser.png': ('noto', 'motorcycle', '巡航摩托'),
    'moped.png': ('noto', 'motor-scooter', '轻便摩托'),
    'sidecar.png': ('noto', 'motorcycle', '边三轮'),
    'quad-bike.png': ('noto', 'racing-motorcycle', '四轮摩托'),

    # === Bicycles ===
    'mountain-bike.png': ('noto', 'mountain-bicyclist', '山地车'),
    'road-bike.png': ('noto', 'bicycle', '公路车'),
    'bmx.png': ('noto', 'bicyclist', '小轮车'),
    'tricycle.png': ('fxemoji', 'tricycle', '三轮车'),
    'tandem-bike.png': ('noto', 'bicycle', '双人自行车'),
    'electric-bike.png': ('noto', 'bicycle', '电动自行车'),
    'kids-bike.png': ('noto', 'bicycle', '儿童自行车'),
    'unicycle.png': ('fxemoji', 'unicycle', '独轮车'),
    'cargo-bike.png': ('noto', 'bicycle', '载货自行车'),

    # === Rail ===
    'diesel-train.png': ('noto', 'locomotive', '内燃机车'),
    'electric-train.png': ('noto', 'high-speed-train', '电力机车'),

    # === Aircraft ===
    'space-shuttle.png': ('noto', 'rocket', '航天飞机'),
    'blimp.png': ('fxemoji', 'blimp', '飞艇'),
    'glider.png': ('noto', 'small-airplane', '滑翔机'),
    'biplane.png': ('noto', 'small-airplane', '双翼飞机'),
    'seaplane.png': ('noto', 'small-airplane', '水上飞机'),
    'cargo-plane.png': ('noto', 'airplane', '货机'),
    'drone.png': ('fxemoji', 'drone', '无人机'),
    'hang-glider.png': ('noto', 'parachute', '悬挂滑翔机'),

    # === Watercraft ===
    'yacht.png': ('noto', 'motor-boat', '游艇'),
    'rowboat.png': ('noto', 'canoe', '划艇'),
    'fishing-boat.png': ('fxemoji', 'fishingboat', '渔船'),
    'tugboat.png': ('fxemoji', 'tugboat', '拖船'),
    'cargo-ship.png': ('noto', 'ship', '货船'),
    'submarine.png': ('fxemoji', 'submarine', '潜水艇'),
    'houseboat.png': ('noto', 'passenger-ship', '船屋'),
    'jet-ski.png': ('fxemoji', 'jetski', '水上摩托'),
    'raft.png': ('noto', 'canoe', '木筏'),
    'lifeboat.png': ('noto', 'motor-boat', '救生艇'),
    'hovercraft.png': ('fxemoji', 'hovercraft', '气垫船'),

    # === Special Vehicles ===
    'golf-cart.png': ('noto', 'automobile', '高尔夫球车'),
    'go-kart.png': ('noto', 'racing-car', '卡丁车'),
    'snowmobile.png': ('fxemoji', 'snowmobile', '雪地摩托'),
    'snow-plow.png': ('noto', 'delivery-truck', '除雪车'),
    'street-sweeper.png': ('noto', 'delivery-truck', '清扫车'),
    'mail-truck.png': ('noto', 'delivery-truck', '邮政车'),
    'camper-van.png': ('fxemoji', 'campervan', '房车'),
    'rv.png': ('noto', 'recreational-vehicle', '旅居车'),
    'stroller.png': ('fxemoji', 'stroller', '婴儿车'),
    'wagon.png': ('fxemoji', 'horsewagon', '马车'),
    'tank.png': ('fxemoji', 'tank', '坦克'),
    'army-truck.png': ('noto', 'delivery-truck', '军用卡车'),
    'amphibious.png': ('noto', 'sport-utility-vehicle', '两栖车'),
}


def download_icon(filename, icon_set, icon_name, chinese_name):
    """Download a single icon from Iconify API"""
    filepath = os.path.join(SAVE_DIR, filename)

    # Skip if exists
    if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
        return True, 'exists'

    # Try PNG from Iconify API
    url = f'https://api.iconify.design/{icon_set}/{icon_name}.svg?width=128&height=128'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'image/svg+xml,image/*,*/*;q=0.8'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()

        # Check if we got valid SVG
        if b'<svg' not in data and b'<?xml' not in data:
            return False, 'not SVG'

        # Save as SVG (will work in browsers)
        svg_path = filepath.replace('.png', '.svg')
        with open(svg_path, 'wb') as f:
            f.write(data)

        return True, 'downloaded'

    except Exception as e:
        return False, str(e)[:30]


def generate_verification_html():
    """Generate HTML page to verify downloaded icons"""
    html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Vehicle Icons Verification</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f5f5f5; }
        h1 { text-align: center; color: #333; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; }
        .card { background: white; border-radius: 10px; padding: 15px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .card img, .card object { width: 64px; height: 64px; margin-bottom: 10px; }
        .card .name { font-size: 12px; color: #333; font-weight: bold; }
        .card .chinese { font-size: 11px; color: #666; }
        .card .file { font-size: 10px; color: #999; word-break: break-all; }
        .card.missing { background: #ffe0e0; }
        .status { text-align: center; margin: 20px 0; padding: 15px; background: white; border-radius: 10px; }
    </style>
</head>
<body>
    <h1>Vehicle Icons Verification Page</h1>
    <div class="status">
        <p>Check each icon to ensure it matches the vehicle name.</p>
        <p>Red background = missing file</p>
    </div>
    <div class="grid">
'''

    for filename, (icon_set, icon_name, chinese) in VEHICLE_ICONS.items():
        svg_file = filename.replace('.png', '.svg')
        svg_path = os.path.join(SAVE_DIR, svg_file)
        exists = os.path.exists(svg_path)

        card_class = '' if exists else 'missing'
        img_tag = f'<object data="images/vehicles/{svg_file}" type="image/svg+xml"></object>' if exists else '<div style="width:64px;height:64px;background:#ddd;margin:0 auto 10px;border-radius:10px;">?</div>'

        html += f'''
        <div class="card {card_class}">
            {img_tag}
            <div class="name">{icon_name}</div>
            <div class="chinese">{chinese}</div>
            <div class="file">{svg_file}</div>
        </div>
'''

    html += '''
    </div>
</body>
</html>
'''

    verify_path = os.path.join(BASE_DIR, 'verify-icons.html')
    with open(verify_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return verify_path


def main():
    print('=' * 50)
    print('Vehicle Icon Download Script (Iconify API)')
    print('=' * 50)
    print(f'\nSave directory: {SAVE_DIR}')
    print(f'Icons to download: {len(VEHICLE_ICONS)}')
    print('\nDownloading...\n')

    success = 0
    fail = 0
    failed_list = []

    for filename, (icon_set, icon_name, chinese) in VEHICLE_ICONS.items():
        ok, status = download_icon(filename, icon_set, icon_name, chinese)
        if ok:
            success += 1
            print(f'  [OK] {filename} ({status})')
        else:
            fail += 1
            failed_list.append((filename, chinese, status))
            print(f'  [FAIL] {filename}: {status}')
        time.sleep(0.2)

    print('\n' + '=' * 50)
    print(f'Done! Success: {success}, Failed: {fail}')

    # Generate verification page
    verify_path = generate_verification_html()
    print(f'\nVerification page created: {verify_path}')
    print('Open this file in browser to check all icons!')

    if failed_list:
        print(f'\nFailed downloads:')
        for fn, ch, st in failed_list:
            print(f'  - {fn} ({ch}): {st}')

    print('=' * 50)


if __name__ == '__main__':
    main()
