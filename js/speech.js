/**
 * 语音合成模块 - 幼儿英语学习游戏
 * 使用 Web Speech API 实现英语发音
 */

const SpeechModule = {
  // 语音合成实例
  synth: window.speechSynthesis,

  // 默认配置
  config: {
    lang: 'en-US',
    rate: 0.75,    // 语速较慢，适合幼儿
    pitch: 1.1,    // 稍高音调，更友好
    volume: 1.0
  },

  // 当前是否正在播放
  isSpeaking: false,

  /**
   * 播放文本
   * @param {string} text - 要播放的文本
   * @param {object} options - 可选配置
   * @returns {Promise} - 播放完成后resolve
   */
  speak(text, options = {}) {
    return new Promise((resolve, reject) => {
      // 如果正在播放，先停止
      if (this.synth.speaking) {
        this.synth.cancel();
      }

      const utterance = new SpeechSynthesisUtterance(text);

      // 合并配置
      const config = { ...this.config, ...options };
      utterance.lang = config.lang;
      utterance.rate = config.rate;
      utterance.pitch = config.pitch;
      utterance.volume = config.volume;

      // 尝试选择更好的声音
      const voices = this.synth.getVoices();
      const preferredVoice = voices.find(v =>
        v.lang.startsWith('en') && v.name.includes('Samantha')
      ) || voices.find(v =>
        v.lang.startsWith('en-US')
      ) || voices.find(v =>
        v.lang.startsWith('en')
      );

      if (preferredVoice) {
        utterance.voice = preferredVoice;
      }

      utterance.onstart = () => {
        this.isSpeaking = true;
      };

      utterance.onend = () => {
        this.isSpeaking = false;
        resolve();
      };

      utterance.onerror = (event) => {
        this.isSpeaking = false;
        // 不reject，避免阻断流程
        console.warn('Speech error:', event.error);
        resolve();
      };

      this.synth.speak(utterance);
    });
  },

  /**
   * 播放中文
   * @param {string} text - 中文文本
   */
  async speakChinese(text) {
    return new Promise((resolve) => {
      if (this.synth.speaking) {
        this.synth.cancel();
      }

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'zh-CN';
      utterance.rate = 0.8;
      utterance.pitch = 1.0;
      utterance.volume = 1.0;

      // 尝试选择中文声音
      const voices = this.synth.getVoices();
      const chineseVoice = voices.find(v => v.lang.includes('zh')) ||
                          voices.find(v => v.lang.includes('cmn'));
      if (chineseVoice) {
        utterance.voice = chineseVoice;
      }

      utterance.onend = () => resolve();
      utterance.onerror = () => resolve();

      this.synth.speak(utterance);
    });
  },

  /**
   * 播放中英文（先英文后中文）
   * @param {string} english - 英文
   * @param {string} chinese - 中文
   */
  async speakBilingual(english, chinese) {
    // 先读英文
    await this.speak(english, { rate: 0.7 });
    // 短暂停顿
    await this.delay(400);
    // 再读中文
    await this.speakChinese(chinese);
  },

  /**
   * 播放字母及其代表单词
   * @param {string} letter - 字母
   * @param {string} word - 代表单词
   */
  async speakLetter(letter, word) {
    // 先读字母
    await this.speak(letter, { rate: 0.6 });
    // 短暂停顿
    await this.delay(300);
    // 再读单词
    await this.speak(word, { rate: 0.7 });
  },

  /**
   * 播放字母单词的中英文
   * @param {string} word - 英文单词
   * @param {string} chinese - 中文翻译
   */
  async speakWord(word, chinese) {
    await this.speakBilingual(word, chinese);
  },

  /**
   * 播放数字
   * @param {number|string} number - 数字
   */
  async speakNumber(number) {
    await this.speak(String(number), { rate: 0.6 });
  },

  /**
   * 播放颜色
   * @param {string} color - 颜色名称
   */
  async speakColor(color) {
    await this.speak(color, { rate: 0.65 });
  },

  /**
   * 播放动物名称
   * @param {string} animal - 动物名称
   */
  async speakAnimal(animal) {
    await this.speak(animal, { rate: 0.7 });
  },

  /**
   * 播放鼓励语
   */
  async speakEncouragement() {
    const phrases = [
      'Great job!',
      'Well done!',
      'Excellent!',
      'You did it!',
      'Amazing!'
    ];
    const phrase = phrases[Math.floor(Math.random() * phrases.length)];
    await this.speak(phrase, { rate: 0.9, pitch: 1.2 });
  },

  /**
   * 播放再试一次提示
   */
  async speakTryAgain() {
    await this.speak('Try again!', { rate: 0.8 });
  },

  /**
   * 停止播放
   */
  stop() {
    this.synth.cancel();
    this.isSpeaking = false;
  },

  /**
   * 延迟函数
   * @param {number} ms - 毫秒数
   */
  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  },

  /**
   * 初始化 - 预加载声音列表
   */
  init() {
    // 某些浏览器需要先获取一次声音列表
    if (this.synth.getVoices().length === 0) {
      this.synth.addEventListener('voiceschanged', () => {
        console.log('Voices loaded:', this.synth.getVoices().length);
      });
    }

    // iOS Safari 需要用户交互后才能播放
    // 在第一次点击时会自动激活
    console.log('Speech module initialized');
  }
};

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', () => {
  SpeechModule.init();
});
