/**
 * 交通工具数据 - 去重版本
 * 每个emoji只对应一个交通工具，避免学习歧义
 * PNG图片来自Twemoji, SVG图片来自Iconify
 */

const VehiclesData = {
  // ==================== 轿车类 ====================
  cars: [
    { name: 'Car', chinese: '汽车', image: 'car.png', emoji: '🚗' },
    { name: 'Taxi', chinese: '出租车', image: 'taxi.png', emoji: '🚕' },
    { name: 'SUV', chinese: '越野车', image: 'suv.png', emoji: '🚙' },
    { name: 'Pickup Truck', chinese: '皮卡车', image: 'pickup-truck.png', emoji: '🛻' },
    { name: 'Racing Car', chinese: '赛车', image: 'racing-car.png', emoji: '🏎️' },
    { name: 'Minivan', chinese: '面包车', image: 'minivan.svg', emoji: '🚐' },
  ],

  // ==================== 卡车类 ====================
  trucks: [
    { name: 'Delivery Truck', chinese: '送货车', image: 'delivery-truck.png', emoji: '🚚' },
    { name: 'Semi Truck', chinese: '半挂车', image: 'articulated-truck.png', emoji: '🚛' },
  ],

  // ==================== 公共交通类 ====================
  publicTransport: [
    { name: 'Bus', chinese: '公交车', image: 'bus.png', emoji: '🚌' },
    { name: 'Trolleybus', chinese: '无轨电车', image: 'trolleybus.png', emoji: '🚎' },
  ],

  // ==================== 特种车辆类 ====================
  emergencyVehicles: [
    { name: 'Ambulance', chinese: '救护车', image: 'ambulance.png', emoji: '🚑' },
    { name: 'Fire Engine', chinese: '消防车', image: 'fire-engine.png', emoji: '🚒' },
    { name: 'Police Car', chinese: '警车', image: 'police-car.png', emoji: '🚓' },
  ],

  // ==================== 摩托车类 ====================
  motorcycles: [
    { name: 'Motorcycle', chinese: '摩托车', image: 'motorcycle.png', emoji: '🏍️' },
    { name: 'Scooter', chinese: '踏板车', image: 'motor-scooter.png', emoji: '🛵' },
  ],

  // ==================== 自行车类 ====================
  bicycles: [
    { name: 'Bicycle', chinese: '自行车', image: 'bicycle.png', emoji: '🚲' },
    { name: 'Kick Scooter', chinese: '滑板车', image: 'kick-scooter.png', emoji: '🛴' },
  ],

  // ==================== 其他陆地车辆 ====================
  otherLand: [
    { name: 'Tractor', chinese: '拖拉机', image: 'tractor.png', emoji: '🚜' },
    { name: 'Rickshaw', chinese: '三轮车', image: 'rickshaw.png', emoji: '🛺' },
    { name: 'Skateboard', chinese: '滑板', image: 'skateboard.png', emoji: '🛹' },
    { name: 'Roller Skate', chinese: '轮滑鞋', image: 'roller-skate.png', emoji: '🛼' },
    { name: 'Sled', chinese: '雪橇', image: 'sled.png', emoji: '🛷' },
    { name: 'Wheelchair', chinese: '轮椅', image: 'wheelchair.png', emoji: '🦽' },
    { name: 'Electric Wheelchair', chinese: '电动轮椅', image: 'motorized-wheelchair.png', emoji: '🦼' },
  ],

  // ==================== 轨道交通类 ====================
  railVehicles: [
    { name: 'Train', chinese: '火车', image: 'train.png', emoji: '🚂' },
    { name: 'High Speed Train', chinese: '高铁', image: 'high-speed-train.png', emoji: '🚄' },
    { name: 'Bullet Train', chinese: '子弹头列车', image: 'bullet-train.png', emoji: '🚅' },
    { name: 'Metro', chinese: '地铁', image: 'metro.png', emoji: '🚇' },
    { name: 'Tram', chinese: '有轨电车', image: 'tram.png', emoji: '🚊' },
    { name: 'Monorail', chinese: '单轨列车', image: 'monorail.png', emoji: '🚝' },
    { name: 'Light Rail', chinese: '轻轨', image: 'light-rail.png', emoji: '🚈' },
    { name: 'Cable Car', chinese: '缆车', image: 'cable-car.png', emoji: '🚡' },
    { name: 'Gondola', chinese: '吊舱缆车', image: 'gondola.png', emoji: '🚠' },
    { name: 'Funicular', chinese: '登山缆车', image: 'funicular.png', emoji: '🚞' },
  ],

  // ==================== 飞行器类 ====================
  aircraft: [
    { name: 'Airplane', chinese: '飞机', image: 'airplane.png', emoji: '✈️' },
    { name: 'Small Airplane', chinese: '小型飞机', image: 'small-airplane.png', emoji: '🛩️' },
    { name: 'Helicopter', chinese: '直升机', image: 'helicopter.png', emoji: '🚁' },
    { name: 'Rocket', chinese: '火箭', image: 'rocket.png', emoji: '🚀' },
    { name: 'UFO', chinese: '飞碟', image: 'flying-saucer.png', emoji: '🛸' },
    { name: 'Parachute', chinese: '降落伞', image: 'parachute.png', emoji: '🪂' },
    { name: 'Hot Air Balloon', chinese: '热气球', image: 'hot-air-balloon.png', emoji: '🎈' },
  ],

  // ==================== 水上交通类 ====================
  watercraft: [
    { name: 'Sailboat', chinese: '帆船', image: 'sailboat.png', emoji: '⛵' },
    { name: 'Speedboat', chinese: '快艇', image: 'speedboat.png', emoji: '🚤' },
    { name: 'Ferry', chinese: '渡轮', image: 'ferry.png', emoji: '⛴️' },
    { name: 'Canoe', chinese: '独木舟', image: 'canoe.png', emoji: '🛶' },
    { name: 'Ship', chinese: '轮船', image: 'cargo-ship.svg', emoji: '🚢' },
    { name: 'Cruise Ship', chinese: '游轮', image: 'houseboat.svg', emoji: '🛳️' },
    { name: 'Rowboat', chinese: '划艇', image: 'rowboat.svg', emoji: '🚣' },
  ],

  // ==================== 交通相关 ====================
  trafficRelated: [
    { name: 'Anchor', chinese: '锚', emoji: '⚓' },
    { name: 'Fuel Pump', chinese: '加油站', emoji: '⛽' },
    { name: 'Traffic Light', chinese: '红绿灯', emoji: '🚦' },
    { name: 'Stop Sign', chinese: '停止标志', emoji: '🛑' },
    { name: 'Construction', chinese: '施工中', emoji: '🚧' },
  ],

  /**
   * 获取所有交通工具列表
   */
  getAllVehicles() {
    return [
      ...this.cars,
      ...this.trucks,
      ...this.publicTransport,
      ...this.emergencyVehicles,
      ...this.motorcycles,
      ...this.bicycles,
      ...this.otherLand,
      ...this.railVehicles,
      ...this.aircraft,
      ...this.watercraft,
      ...this.trafficRelated
    ];
  },

  /**
   * 获取分类数据
   */
  getCategories() {
    return [
      { key: 'cars', name: 'Cars', chinese: '轿车', emoji: '🚗', data: this.cars },
      { key: 'trucks', name: 'Trucks', chinese: '卡车', emoji: '🚚', data: this.trucks },
      { key: 'publicTransport', name: 'Buses', chinese: '巴士', emoji: '🚌', data: this.publicTransport },
      { key: 'emergencyVehicles', name: 'Emergency', chinese: '特种车辆', emoji: '🚑', data: this.emergencyVehicles },
      { key: 'motorcycles', name: 'Motorcycles', chinese: '摩托车', emoji: '🏍️', data: this.motorcycles },
      { key: 'bicycles', name: 'Bicycles', chinese: '自行车', emoji: '🚲', data: this.bicycles },
      { key: 'otherLand', name: 'Other Land', chinese: '其他陆地', emoji: '🚜', data: this.otherLand },
      { key: 'railVehicles', name: 'Trains', chinese: '火车', emoji: '🚂', data: this.railVehicles },
      { key: 'aircraft', name: 'Aircraft', chinese: '飞行器', emoji: '✈️', data: this.aircraft },
      { key: 'watercraft', name: 'Boats', chinese: '船只', emoji: '⛵', data: this.watercraft },
      { key: 'trafficRelated', name: 'Others', chinese: '其他', emoji: '🎯', data: this.trafficRelated },
    ];
  },

  /**
   * 获取所有有图片的车辆（用于测验）
   */
  getVehiclesWithImages() {
    return this.getAllVehicles().filter(v => v.image);
  },

  /**
   * 获取所有有emoji的车辆
   */
  getVehiclesWithEmoji() {
    return this.getAllVehicles().filter(v => v.emoji);
  },

  /**
   * 获取随机测验题目
   */
  getQuizQuestion(count = 3) {
    const vehicles = this.getVehiclesWithImages();
    const shuffled = [...vehicles].sort(() => Math.random() - 0.5);
    const correct = shuffled[0];
    const options = shuffled.slice(0, count).sort(() => Math.random() - 0.5);
    return { correct, options };
  }
};

// 统计
console.log('Total vehicles:', VehiclesData.getAllVehicles().length);
console.log('With images:', VehiclesData.getVehiclesWithImages().length);
console.log('With emoji:', VehiclesData.getVehiclesWithEmoji().length);
