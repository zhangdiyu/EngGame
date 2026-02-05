#!/usr/bin/env python3
"""
Construction Vehicles Image Download Script
从 Wikimedia Commons 爬取 Construction vehicles 分类下的图片
动态获取页面图片，筛选工程车相关图片并下载
"""

import os
import re
import urllib.request
import urllib.parse
import ssl
import time
import sys
import json
from html.parser import HTMLParser

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Save directory
SAVE_DIR = os.path.join(os.path.dirname(__file__), 'images', 'vehicles')

# Ensure directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Wikimedia Commons API endpoint
WIKI_API = 'https://commons.wikimedia.org/w/api.php'

# 工程车关键词列表（用于筛选）
CONSTRUCTION_KEYWORDS = [
    # 挖掘机类
    'excavator', 'digger', 'backhoe', 'mini excavator',
    # 推土机类
    'bulldozer', 'dozer',
    # 装载机类
    'loader', 'front loader', 'wheel loader', 'skid steer', 'bobcat', 'telehandler',
    # 起重机类
    'crane', 'tower crane', 'mobile crane', 'crawler crane', 'truck crane',
    # 压路机类
    'roller', 'road roller', 'compactor', 'steamroller', 'vibratory roller',
    # 搅拌车类
    'mixer', 'cement mixer', 'concrete mixer', 'cement truck', 'agitator',
    # 自卸车类
    'dump truck', 'dumper', 'tipper', 'hauler', 'articulated hauler',
    # 平地机类
    'grader', 'motor grader',
    # 铺路机类
    'paver', 'asphalt paver', 'road paver',
    # 打桩机类
    'pile driver', 'piling', 'pile hammer',
    # 叉车类
    'forklift', 'fork lift', 'reach stacker',
    # 泵车类
    'concrete pump', 'pump truck', 'boom pump',
    # 钻机类
    'drilling rig', 'drill', 'boring machine',
    # 其他工程车
    'construction vehicle', 'construction equipment',
    'earthmover', 'earth mover', 'earth moving',
    'tractor', 'scraper', 'trencher',
    'asphalt', 'paving', 'road construction',
]

# 中文名称映射
CHINESE_NAMES = {
    'excavator': '挖掘机',
    'digger': '挖掘机',
    'backhoe': '反铲挖掘机',
    'mini excavator': '小型挖掘机',
    'bulldozer': '推土机',
    'dozer': '推土机',
    'loader': '装载机',
    'front loader': '前装载机',
    'wheel loader': '轮式装载机',
    'skid steer': '滑移装载机',
    'bobcat': '山猫装载机',
    'telehandler': '伸缩臂叉装车',
    'crane': '起重机',
    'tower crane': '塔式起重机',
    'mobile crane': '移动起重机',
    'crawler crane': '履带起重机',
    'truck crane': '汽车起重机',
    'roller': '压路机',
    'road roller': '压路机',
    'compactor': '压实机',
    'steamroller': '蒸汽压路机',
    'vibratory roller': '振动压路机',
    'mixer': '搅拌车',
    'cement mixer': '水泥搅拌车',
    'concrete mixer': '混凝土搅拌车',
    'cement truck': '水泥车',
    'agitator': '搅拌车',
    'dump truck': '自卸车',
    'dumper': '自卸车',
    'tipper': '翻斗车',
    'hauler': '运输车',
    'articulated hauler': '铰接式运输车',
    'grader': '平地机',
    'motor grader': '平地机',
    'paver': '铺路机',
    'asphalt paver': '沥青铺路机',
    'road paver': '铺路机',
    'pile driver': '打桩机',
    'piling': '打桩机',
    'pile hammer': '打桩锤',
    'forklift': '叉车',
    'fork lift': '叉车',
    'reach stacker': '正面吊',
    'concrete pump': '混凝土泵车',
    'pump truck': '泵车',
    'boom pump': '臂架泵车',
    'drilling rig': '钻机',
    'drill': '钻机',
    'boring machine': '掘进机',
    'earthmover': '土方机械',
    'earth mover': '土方机械',
    'earth moving': '土方机械',
    'tractor': '拖拉机',
    'scraper': '铲运机',
    'trencher': '挖沟机',
    'asphalt': '沥青设备',
    'paving': '铺路设备',
    'road construction': '道路施工车',
}

def get_category_images(category_name, limit=100):
    """
    使用 Wikimedia Commons API 获取分类下的图片列表
    """
    images = []
    continue_param = None

    while len(images) < limit:
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': f'Category:{category_name}',
            'cmtype': 'file',
            'cmlimit': min(50, limit - len(images)),
            'format': 'json',
        }

        if continue_param:
            params['cmcontinue'] = continue_param

        url = f"{WIKI_API}?{urllib.parse.urlencode(params)}"

        try:
            headers = {
                'User-Agent': 'KidsEnglishFun/1.0 (Educational Project; Python)'
            }
            request = urllib.request.Request(url, headers=headers)

            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.loads(response.read().decode('utf-8'))

            if 'query' in data and 'categorymembers' in data['query']:
                for member in data['query']['categorymembers']:
                    images.append(member['title'])

            # Check for continuation
            if 'continue' in data and 'cmcontinue' in data['continue']:
                continue_param = data['continue']['cmcontinue']
            else:
                break

        except Exception as e:
            print(f'  [ERROR] Failed to fetch category: {e}')
            break

    return images

def get_image_url(filename):
    """
    获取图片的实际下载URL
    """
    params = {
        'action': 'query',
        'titles': filename,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'iiurlwidth': 256,  # 获取缩略图URL，适合学习应用
        'format': 'json',
    }

    url = f"{WIKI_API}?{urllib.parse.urlencode(params)}"

    try:
        headers = {
            'User-Agent': 'KidsEnglishFun/1.0 (Educational Project; Python)'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        pages = data.get('query', {}).get('pages', {})
        for page_id, page_info in pages.items():
            if 'imageinfo' in page_info:
                info = page_info['imageinfo'][0]
                # 优先使用缩略图URL
                return info.get('thumburl') or info.get('url')

    except Exception as e:
        print(f'  [ERROR] Failed to get image URL: {e}')

    return None

def extract_vehicle_name(wiki_title):
    """
    从Wiki标题提取车辆名称
    例如: "File:Yellow excavator in action.jpg" -> "excavator"
    """
    # 移除 "File:" 前缀和文件扩展名
    name = wiki_title.replace('File:', '')
    name = re.sub(r'\.(jpg|jpeg|png|gif|svg|webp)$', '', name, flags=re.IGNORECASE)

    # 转小写用于匹配
    name_lower = name.lower()

    # 检查是否匹配工程车关键词
    matched_keyword = None
    for keyword in CONSTRUCTION_KEYWORDS:
        if keyword in name_lower:
            matched_keyword = keyword
            break

    return name, matched_keyword

def create_safe_filename(name, keyword):
    """
    创建安全的文件名
    """
    # 使用匹配的关键词作为基础名称
    base_name = keyword.replace(' ', '-')
    return f"construction-{base_name}.png"

def download_image(url, filename):
    """
    下载图片
    """
    filepath = os.path.join(SAVE_DIR, filename)

    # Skip if file exists
    if os.path.exists(filepath):
        print(f'  [SKIP] {filename} exists')
        return True, filepath

    try:
        headers = {
            'User-Agent': 'KidsEnglishFun/1.0 (Educational Project; Python)',
            'Accept': 'image/*,*/*;q=0.8',
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()

        # Verify it's actually an image
        if len(data) < 100:
            raise Exception('File too small')

        with open(filepath, 'wb') as f:
            f.write(data)

        print(f'  [OK] {filename}')
        return True, filepath

    except Exception as e:
        print(f'  [FAIL] {filename}: {str(e)[:40]}')
        return False, None

def generate_js_data(downloaded_vehicles):
    """
    生成 JavaScript 数据格式
    """
    js_entries = []
    for vehicle in downloaded_vehicles:
        name = vehicle['name']
        chinese = vehicle['chinese']
        image = vehicle['filename']

        # 格式化名称: construction-excavator -> Excavator
        display_name = name.replace('construction-', '').replace('-', ' ').title()

        js_entries.append(
            f"    {{ name: '{display_name}', chinese: '{chinese}', image: '{image}', emoji: '🚧' }}"
        )

    return js_entries

def get_subcategories(category_name):
    """
    获取子分类列表
    """
    subcategories = []
    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': f'Category:{category_name}',
        'cmtype': 'subcat',
        'cmlimit': 50,
        'format': 'json',
    }

    url = f"{WIKI_API}?{urllib.parse.urlencode(params)}"

    try:
        headers = {
            'User-Agent': 'KidsEnglishFun/1.0 (Educational Project; Python)'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        if 'query' in data and 'categorymembers' in data['query']:
            for member in data['query']['categorymembers']:
                # 提取分类名称（去掉 "Category:" 前缀）
                cat_name = member['title'].replace('Category:', '')
                subcategories.append(cat_name)

    except Exception as e:
        print(f'  [ERROR] Failed to fetch subcategories: {e}')

    return subcategories

def main():
    print('=' * 60)
    print('Construction Vehicles Image Download Script')
    print('从 Wikimedia Commons 爬取工程车图片')
    print('=' * 60)
    print(f'\nSave directory: {SAVE_DIR}')

    # Step 1: 获取分类和子分类下的所有图片
    print('\n[Step 1] Fetching images from Wikimedia Commons...')

    # 主分类
    category_images = get_category_images('Construction_vehicles', limit=200)
    print(f'  Found {len(category_images)} images in main category')

    # 获取子分类
    subcategories = get_subcategories('Construction_vehicles')
    print(f'  Found {len(subcategories)} subcategories')

    # 从相关子分类获取更多图片
    relevant_subcats = [
        'Excavators', 'Bulldozers', 'Wheel_loaders', 'Cranes_(machine)',
        'Roller_compactors', 'Concrete_mixer_trucks', 'Dump_trucks',
        'Backhoe_loaders', 'Forklifts', 'Motor_graders',
        # 更多子分类
        'Articulated_haulers', 'Asphalt_pavers', 'Concrete_pumps',
        'Crawler_cranes', 'Mobile_cranes', 'Tower_cranes',
        'Mini_excavators', 'Skid-steer_loaders', 'Telehandlers',
        'Pile_drivers', 'Road_rollers', 'Steamrollers',
        'Scrapers_(machines)', 'Trenchers', 'Drilling_rigs'
    ]

    for subcat in relevant_subcats:
        sub_images = get_category_images(subcat, limit=50)
        category_images.extend(sub_images)
        print(f'  + {len(sub_images)} images from {subcat}')

    # 去重
    category_images = list(set(category_images))
    print(f'  Total unique images: {len(category_images)}')

    # Step 2: 筛选匹配工程车关键词的图片
    print('\n[Step 2] Filtering construction vehicle images...')
    matched_images = []
    seen_keywords = set()  # 避免重复下载同类型车辆

    for wiki_title in category_images:
        name, keyword = extract_vehicle_name(wiki_title)
        if keyword and keyword not in seen_keywords:
            matched_images.append({
                'wiki_title': wiki_title,
                'name': name,
                'keyword': keyword,
                'chinese': CHINESE_NAMES.get(keyword, '工程车'),
            })
            seen_keywords.add(keyword)
            print(f'  [MATCH] {keyword}: {name[:50]}...')

    print(f'\n  Matched {len(matched_images)} unique vehicle types')

    # Step 3: 下载图片
    print('\n[Step 3] Downloading images...')
    downloaded_vehicles = []

    for item in matched_images:
        # 获取图片URL
        image_url = get_image_url(item['wiki_title'])
        if not image_url:
            print(f'  [SKIP] Could not get URL for: {item["keyword"]}')
            continue

        # 生成文件名
        filename = create_safe_filename(item['name'], item['keyword'])

        # 下载
        success, filepath = download_image(image_url, filename)
        if success:
            downloaded_vehicles.append({
                'name': item['keyword'],
                'chinese': item['chinese'],
                'filename': filename,
            })

        time.sleep(3)  # 增加延迟避免速率限制

    # Step 4: 生成 JavaScript 数据
    print('\n[Step 4] Generating JavaScript data...')
    js_entries = generate_js_data(downloaded_vehicles)

    print('\n' + '=' * 60)
    print('Generated JavaScript data for vehicles-data.js:')
    print('=' * 60)
    print('\n  // ==================== 工程车类 ====================')
    print('  constructionVehicles: [')
    for entry in js_entries:
        print(entry + ',')
    print('  ],')

    # 保存到文件
    output_file = os.path.join(os.path.dirname(__file__), 'construction_vehicles_data.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(downloaded_vehicles, f, ensure_ascii=False, indent=2)
    print(f'\n[INFO] Data saved to: {output_file}')

    print('\n' + '=' * 60)
    print(f'Done! Downloaded: {len(downloaded_vehicles)} vehicle images')
    print('=' * 60)

    return downloaded_vehicles

if __name__ == '__main__':
    main()
