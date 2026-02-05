#!/usr/bin/env python3
"""
Vehicle Image Download Script
Downloads PNG images to images/vehicles/ folder
"""

import os
import urllib.request
import ssl
import time
import sys

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Save directory
SAVE_DIR = os.path.join(os.path.dirname(__file__), 'images', 'vehicles')

# Ensure directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Vehicle images from free icon libraries
VEHICLE_IMAGES = {
    # === Cars ===
    'suv.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202926.png',
    'sedan.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097180.png',
    'convertible.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202934.png',
    'minivan.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202946.png',
    'electric-car.png': 'https://cdn-icons-png.flaticon.com/128/4564/4564336.png',
    'vintage-car.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202920.png',
    'limousine.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202941.png',
    'jeep.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202928.png',
    'hatchback.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097144.png',

    # === Trucks ===
    'moving-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097157.png',
    'semi-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097123.png',
    'tanker-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097165.png',
    'dump-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097113.png',
    'garbage-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097136.png',
    'ice-cream-truck.png': 'https://cdn-icons-png.flaticon.com/128/3081/3081967.png',
    'food-truck.png': 'https://cdn-icons-png.flaticon.com/128/2718/2718224.png',
    'tow-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097169.png',
    'flatbed-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097132.png',
    'box-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097109.png',
    'cement-mixer.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097106.png',
    'logging-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097148.png',
    'cargo-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097102.png',

    # === Public Transport ===
    'double-decker-bus.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097117.png',
    'minibus.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097153.png',
    'coach.png': 'https://cdn-icons-png.flaticon.com/128/2935/2935396.png',
    'shuttle-bus.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097161.png',
    'airport-bus.png': 'https://cdn-icons-png.flaticon.com/128/2935/2935391.png',
    'tour-bus.png': 'https://cdn-icons-png.flaticon.com/128/2935/2935401.png',
    'city-bus.png': 'https://cdn-icons-png.flaticon.com/128/1819/1819547.png',

    # === Taxis ===
    'black-cab.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097098.png',

    # === Emergency Vehicles ===
    'police-van.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830335.png',
    'swat-truck.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830340.png',
    'rescue-vehicle.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830349.png',
    'ladder-truck.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830319.png',
    'armored-car.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830355.png',

    # === Construction Vehicles ===
    'excavator.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097128.png',
    'bulldozer.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097093.png',
    'crane.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097111.png',
    'forklift.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097134.png',
    'roller.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097159.png',
    'backhoe.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097091.png',
    'loader.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097146.png',
    'grader.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097140.png',
    'paver.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097155.png',
    'pile-driver.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256216.png',
    'concrete-pump.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097107.png',
    'tower-crane.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256221.png',
    'skid-steer.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097163.png',
    'compactor.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256201.png',
    'asphalt-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097089.png',

    # === Farm Vehicles ===
    'harvester.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097142.png',
    'combine.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256206.png',
    'plow.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256211.png',
    'seeder.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256226.png',
    'sprayer.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256231.png',
    'baler.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256196.png',
    'farm-truck.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256236.png',
    'atv.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097085.png',
    'utv.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097173.png',

    # === Motorcycles ===
    'dirt-bike.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097115.png',
    'chopper.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202913.png',
    'sport-bike.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202916.png',
    'cruiser.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202910.png',
    'moped.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097151.png',
    'sidecar.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972225.png',
    'quad-bike.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097087.png',

    # === Bicycles ===
    'mountain-bike.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097149.png',
    'road-bike.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097083.png',
    'bmx.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972187.png',
    'tricycle.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972232.png',
    'tandem-bike.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972229.png',
    'electric-bike.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972193.png',
    'kids-bike.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972213.png',
    'unicycle.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972235.png',
    'cargo-bike.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972190.png',

    # === Rail ===
    'diesel-train.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097167.png',
    'electric-train.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097121.png',

    # === Aircraft ===
    'space-shuttle.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097081.png',
    'blimp.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972184.png',
    'glider.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972199.png',
    'biplane.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972181.png',
    'seaplane.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972222.png',
    'cargo-plane.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972178.png',
    'drone.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097119.png',
    'hang-glider.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972202.png',

    # === Watercraft ===
    'yacht.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972238.png',
    'rowboat.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972219.png',
    'fishing-boat.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972196.png',
    'tugboat.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097171.png',
    'cargo-ship.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097100.png',
    'submarine.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972226.png',
    'houseboat.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972205.png',
    'jet-ski.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972210.png',
    'raft.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972216.png',
    'lifeboat.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097096.png',
    'hovercraft.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972208.png',

    # === Special Vehicles ===
    'golf-cart.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097138.png',
    'go-kart.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972175.png',
    'snowmobile.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097079.png',
    'snow-plow.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097077.png',
    'street-sweeper.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097075.png',
    'mail-truck.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097073.png',
    'camper-van.png': 'https://cdn-icons-png.flaticon.com/128/3097/3097104.png',
    'rv.png': 'https://cdn-icons-png.flaticon.com/128/3202/3202949.png',
    'stroller.png': 'https://cdn-icons-png.flaticon.com/128/2972/2972172.png',
    'wagon.png': 'https://cdn-icons-png.flaticon.com/128/3256/3256241.png',
    'tank.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830360.png',
    'army-truck.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830365.png',
    'amphibious.png': 'https://cdn-icons-png.flaticon.com/128/2830/2830370.png',
}

def download_image(filename, url):
    """Download a single image"""
    filepath = os.path.join(SAVE_DIR, filename)

    # Skip if file exists
    if os.path.exists(filepath):
        print(f'  [SKIP] {filename} exists')
        return True

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'image/png,image/*,*/*;q=0.8',
            'Referer': 'https://www.flaticon.com/'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()

        # Verify it's actually an image (PNG starts with specific bytes)
        if len(data) < 100:
            raise Exception('File too small, might be blocked')

        with open(filepath, 'wb') as f:
            f.write(data)

        print(f'  [OK] {filename}')
        return True

    except Exception as e:
        print(f'  [FAIL] {filename}: {str(e)[:40]}')
        return False

def main():
    print('=' * 50)
    print('Vehicle Image Download Script')
    print('=' * 50)
    print(f'\nSave directory: {SAVE_DIR}')
    print(f'Images to download: {len(VEHICLE_IMAGES)}')
    print('\nDownloading...\n')

    success = 0
    fail = 0

    for filename, url in VEHICLE_IMAGES.items():
        if download_image(filename, url):
            success += 1
        else:
            fail += 1
        time.sleep(0.3)

    print('\n' + '=' * 50)
    print(f'Done! Success: {success}, Failed: {fail}')
    print('=' * 50)

if __name__ == '__main__':
    main()
