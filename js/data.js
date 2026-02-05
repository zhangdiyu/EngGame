/**
 * 学习内容数据 - 幼儿英语学习游戏
 * 包含字母、数字、颜色、动物的数据定义
 */

const LearningData = {
  // 26个字母及代表单词（含中文翻译）
  letters: [
    { letter: 'A', word: 'Apple', chinese: '苹果', icon: 'fa-apple-whole', emoji: '🍎', color: '#e74c3c' },
    { letter: 'B', word: 'Ball', chinese: '球', icon: 'fa-baseball', emoji: '⚽', color: '#3498db' },
    { letter: 'C', word: 'Cat', chinese: '猫', icon: 'fa-cat', emoji: '🐱', color: '#f39c12' },
    { letter: 'D', word: 'Dog', chinese: '狗', icon: 'fa-dog', emoji: '🐶', color: '#8b4513' },
    { letter: 'E', word: 'Elephant', chinese: '大象', icon: 'fa-elephant', emoji: '🐘', color: '#95a5a6' },
    { letter: 'F', word: 'Fish', chinese: '鱼', icon: 'fa-fish', emoji: '🐟', color: '#1abc9c' },
    { letter: 'G', word: 'Gift', chinese: '礼物', icon: 'fa-gift', emoji: '🎁', color: '#9b59b6' },
    { letter: 'H', word: 'House', chinese: '房子', icon: 'fa-house', emoji: '🏠', color: '#e67e22' },
    { letter: 'I', word: 'Ice cream', chinese: '冰淇淋', icon: 'fa-ice-cream', emoji: '🍦', color: '#ff69b4' },
    { letter: 'J', word: 'Jet', chinese: '喷气机', icon: 'fa-jet-fighter', emoji: '✈️', color: '#34495e' },
    { letter: 'K', word: 'Key', chinese: '钥匙', icon: 'fa-key', emoji: '🔑', color: '#f1c40f' },
    { letter: 'L', word: 'Lemon', chinese: '柠檬', icon: 'fa-lemon', emoji: '🍋', color: '#f1c40f' },
    { letter: 'M', word: 'Moon', chinese: '月亮', icon: 'fa-moon', emoji: '🌙', color: '#bdc3c7' },
    { letter: 'N', word: 'Note', chinese: '音符', icon: 'fa-music', emoji: '🎵', color: '#2ecc71' },
    { letter: 'O', word: 'Orange', chinese: '橙子', icon: 'fa-orange', emoji: '🍊', color: '#e67e22' },
    { letter: 'P', word: 'Plane', chinese: '飞机', icon: 'fa-plane', emoji: '✈️', color: '#3498db' },
    { letter: 'Q', word: 'Queen', chinese: '女王', icon: 'fa-chess-queen', emoji: '👸', color: '#9b59b6' },
    { letter: 'R', word: 'Rainbow', chinese: '彩虹', icon: 'fa-rainbow', emoji: '🌈', color: '#e74c3c' },
    { letter: 'S', word: 'Star', chinese: '星星', icon: 'fa-star', emoji: '⭐', color: '#f1c40f' },
    { letter: 'T', word: 'Tree', chinese: '树', icon: 'fa-tree', emoji: '🌳', color: '#27ae60' },
    { letter: 'U', word: 'Umbrella', chinese: '雨伞', icon: 'fa-umbrella', emoji: '☂️', color: '#9b59b6' },
    { letter: 'V', word: 'Van', chinese: '货车', icon: 'fa-van-shuttle', emoji: '🚐', color: '#e74c3c' },
    { letter: 'W', word: 'Water', chinese: '水', icon: 'fa-water', emoji: '💧', color: '#3498db' },
    { letter: 'X', word: 'X-ray', chinese: 'X光', icon: 'fa-x-ray', emoji: '🩻', color: '#7f8c8d' },
    { letter: 'Y', word: 'Yacht', chinese: '游艇', icon: 'fa-sailboat', emoji: '⛵', color: '#1abc9c' },
    { letter: 'Z', word: 'Zebra', chinese: '斑马', icon: 'fa-horse', emoji: '🦓', color: '#2c3e50' }
  ],

  // 数字1-10
  numbers: [
    { number: 1, word: 'One', chinese: '一', emoji: '1️⃣', icon: 'fa-1', dots: 1 },
    { number: 2, word: 'Two', chinese: '二', emoji: '2️⃣', icon: 'fa-2', dots: 2 },
    { number: 3, word: 'Three', chinese: '三', emoji: '3️⃣', icon: 'fa-3', dots: 3 },
    { number: 4, word: 'Four', chinese: '四', emoji: '4️⃣', icon: 'fa-4', dots: 4 },
    { number: 5, word: 'Five', chinese: '五', emoji: '5️⃣', icon: 'fa-5', dots: 5 },
    { number: 6, word: 'Six', chinese: '六', emoji: '6️⃣', icon: 'fa-6', dots: 6 },
    { number: 7, word: 'Seven', chinese: '七', emoji: '7️⃣', icon: 'fa-7', dots: 7 },
    { number: 8, word: 'Eight', chinese: '八', emoji: '8️⃣', icon: 'fa-8', dots: 8 },
    { number: 9, word: 'Nine', chinese: '九', emoji: '9️⃣', icon: 'fa-9', dots: 9 },
    { number: 10, word: 'Ten', chinese: '十', emoji: '🔟', icon: 'fa-10', dots: 10 }
  ],

  // 8种基础颜色（含中文）
  colors: [
    { name: 'Red', chinese: '红色', hex: '#e74c3c', icon: 'fa-heart', emoji: '❤️' },
    { name: 'Orange', chinese: '橙色', hex: '#e67e22', icon: 'fa-orange', emoji: '🧡' },
    { name: 'Yellow', chinese: '黄色', hex: '#f1c40f', icon: 'fa-sun', emoji: '💛' },
    { name: 'Green', chinese: '绿色', hex: '#27ae60', icon: 'fa-leaf', emoji: '💚' },
    { name: 'Blue', chinese: '蓝色', hex: '#3498db', icon: 'fa-droplet', emoji: '💙' },
    { name: 'Purple', chinese: '紫色', hex: '#9b59b6', icon: 'fa-gem', emoji: '💜' },
    { name: 'Pink', chinese: '粉色', hex: '#ff69b4', icon: 'fa-heart', emoji: '💗' },
    { name: 'Black', chinese: '黑色', hex: '#2c3e50', icon: 'fa-circle', emoji: '🖤' }
  ],

  // 12种常见动物（含中文）
  animals: [
    { name: 'Cat', chinese: '猫', icon: 'fa-cat', emoji: '🐱', color: '#f39c12' },
    { name: 'Dog', chinese: '狗', icon: 'fa-dog', emoji: '🐶', color: '#8b4513' },
    { name: 'Bird', chinese: '鸟', icon: 'fa-dove', emoji: '🐦', color: '#3498db' },
    { name: 'Fish', chinese: '鱼', icon: 'fa-fish', emoji: '🐟', color: '#1abc9c' },
    { name: 'Horse', chinese: '马', icon: 'fa-horse', emoji: '🐴', color: '#8b4513' },
    { name: 'Cow', chinese: '牛', icon: 'fa-cow', emoji: '🐮', color: '#2c3e50' },
    { name: 'Pig', chinese: '猪', icon: 'fa-piggy-bank', emoji: '🐷', color: '#ff69b4' },
    { name: 'Frog', chinese: '青蛙', icon: 'fa-frog', emoji: '🐸', color: '#27ae60' },
    { name: 'Spider', chinese: '蜘蛛', icon: 'fa-spider', emoji: '🕷️', color: '#2c3e50' },
    { name: 'Butterfly', chinese: '蝴蝶', icon: 'fa-butterfly', emoji: '🦋', color: '#9b59b6' },
    { name: 'Rabbit', chinese: '兔子', icon: 'fa-rabbit', emoji: '🐰', color: '#ff69b4' },
    { name: 'Dragon', chinese: '龙', icon: 'fa-dragon', emoji: '🐲', color: '#e74c3c' }
  ],

  // 交通工具（含中文）- 包含工程车
  vehicles: [
    // 常见交通工具
    { name: 'Car', chinese: '汽车', emoji: '🚗', color: '#e74c3c' },
    { name: 'Bus', chinese: '公交车', emoji: '🚌', color: '#f39c12' },
    { name: 'Truck', chinese: '卡车', emoji: '🚚', color: '#3498db' },
    { name: 'Motorcycle', chinese: '摩托车', emoji: '🏍️', color: '#2c3e50' },
    { name: 'Bicycle', chinese: '自行车', emoji: '🚲', color: '#27ae60' },
    { name: 'Train', chinese: '火车', emoji: '🚂', color: '#8b4513' },
    { name: 'Airplane', chinese: '飞机', emoji: '✈️', color: '#3498db' },
    { name: 'Helicopter', chinese: '直升机', emoji: '🚁', color: '#1abc9c' },
    { name: 'Boat', chinese: '船', emoji: '⛵', color: '#3498db' },
    { name: 'Ship', chinese: '轮船', emoji: '🚢', color: '#34495e' },
    { name: 'Rocket', chinese: '火箭', emoji: '🚀', color: '#e74c3c' },
    { name: 'Ambulance', chinese: '救护车', emoji: '🚑', color: '#e74c3c' },
    { name: 'Fire Truck', chinese: '消防车', emoji: '🚒', color: '#c0392b' },
    { name: 'Police Car', chinese: '警车', emoji: '🚓', color: '#2c3e50' },
    { name: 'Taxi', chinese: '出租车', emoji: '🚕', color: '#f1c40f' },
    { name: 'Tractor', chinese: '拖拉机', emoji: '🚜', color: '#27ae60' },
    // 工程车
    { name: 'Excavator', chinese: '挖掘机', emoji: '🚧', color: '#f39c12', image: 'construction-excavator.png' },
    { name: 'Bulldozer', chinese: '推土机', emoji: '🚧', color: '#f39c12', image: 'construction-bulldozer.png' },
    { name: 'Crane', chinese: '起重机', emoji: '🏗️', color: '#e67e22', image: 'construction-crane.png' },
    { name: 'Loader', chinese: '装载机', emoji: '🚧', color: '#f39c12', image: 'construction-loader.png' },
    { name: 'Roller', chinese: '压路机', emoji: '🚧', color: '#f39c12', image: 'construction-roller.png' },
    { name: 'Mixer', chinese: '搅拌车', emoji: '🚧', color: '#3498db', image: 'construction-mixer.png' },
    { name: 'Forklift', chinese: '叉车', emoji: '🚧', color: '#f39c12', image: 'construction-forklift.png' },
    { name: 'Dump Truck', chinese: '自卸车', emoji: '🚧', color: '#e67e22', image: 'construction-dump-truck.png' },
    { name: 'Drilling Rig', chinese: '钻机', emoji: '🚧', color: '#8b4513', image: 'construction-drilling-rig.png' },
    { name: 'Concrete Pump', chinese: '混凝土泵车', emoji: '🚧', color: '#3498db', image: 'construction-concrete-pump.png' },
  ],

  /**
   * 获取随机题目（用于测验）
   * @param {string} category - 类别：letters, numbers, colors, animals
   * @param {number} count - 选项数量
   * @returns {object} - { correct: 正确答案, options: 选项数组 }
   */
  getQuizQuestion(category, count = 3) {
    const data = this[category];
    if (!data || data.length < count) return null;

    // 随机选择正确答案
    const shuffled = [...data].sort(() => Math.random() - 0.5);
    const correct = shuffled[0];
    const options = shuffled.slice(0, count).sort(() => Math.random() - 0.5);

    return { correct, options, category };
  },

  /**
   * 获取发音文本
   */
  getSpeakText(item, category) {
    switch (category) {
      case 'letters':
        return item.word;
      case 'numbers':
        return item.word;
      case 'colors':
        return item.name;
      case 'animals':
        return item.name;
      case 'vehicles':
        return item.name;
      default:
        return '';
    }
  },

  /**
   * 获取中文翻译
   */
  getChineseText(item, category) {
    switch (category) {
      case 'letters':
        return item.chinese;
      case 'colors':
        return item.chinese || '';
      case 'animals':
        return item.chinese;
      case 'vehicles':
        return item.chinese;
      default:
        return '';
    }
  }
};
