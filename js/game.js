/**
 * 测验游戏逻辑 - 幼儿英语学习游戏
 */

const QuizGame = {
  // 当前状态
  currentCategory: 'letters',
  currentQuestion: null,
  score: 0,
  isAnswered: false,

  // DOM元素
  elements: {
    optionsGrid: null,
    playSoundBtn: null,
    scoreDisplay: null,
    rewardPopup: null,
    rewardText: null,
    categoryBtns: null
  },

  /**
   * 初始化游戏
   */
  init() {
    // 获取DOM元素
    this.elements.optionsGrid = document.getElementById('optionsGrid');
    this.elements.playSoundBtn = document.getElementById('playSoundBtn');
    this.elements.scoreDisplay = document.getElementById('scoreDisplay');
    this.elements.rewardPopup = document.getElementById('rewardPopup');
    this.elements.rewardText = document.getElementById('rewardText');
    this.elements.categoryBtns = document.querySelectorAll('.category-btn');

    // 绑定事件
    this.bindEvents();

    // 加载第一题
    this.loadQuestion();
  },

  /**
   * 绑定事件监听
   */
  bindEvents() {
    // 播放声音按钮
    this.elements.playSoundBtn.addEventListener('click', () => {
      this.playCurrentSound();
    });

    // 类别切换按钮
    this.elements.categoryBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // 更新活跃状态
        this.elements.categoryBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // 切换类别并加载新题目
        this.currentCategory = btn.dataset.category;
        this.loadQuestion();
      });
    });

    // 点击奖励弹窗关闭
    this.elements.rewardPopup.addEventListener('click', () => {
      this.hideReward();
      this.loadQuestion();
    });
  },

  /**
   * 加载新题目
   */
  loadQuestion() {
    this.isAnswered = false;

    // 获取题目数据
    const optionCount = this.currentCategory === 'letters' ? 4 : 3;
    this.currentQuestion = LearningData.getQuizQuestion(this.currentCategory, optionCount);

    if (!this.currentQuestion) {
      console.error('Failed to generate question');
      return;
    }

    // 渲染选项
    this.renderOptions();

    // 自动播放声音
    setTimeout(() => {
      this.playCurrentSound();
    }, 500);
  },

  /**
   * 渲染选项
   */
  renderOptions() {
    const { options, category } = this.currentQuestion;
    this.elements.optionsGrid.innerHTML = '';

    options.forEach(item => {
      const card = document.createElement('div');
      card.className = 'option-card';

      // 根据类别渲染不同内容
      switch (category) {
        case 'letters':
          card.innerHTML = `
            <div class="option-icon">${item.emoji}</div>
            <div class="option-text">${item.letter}</div>
          `;
          break;

        case 'numbers':
          card.innerHTML = `
            <div class="option-number">${item.number}</div>
            <div class="option-text">${item.word}</div>
          `;
          break;

        case 'colors':
          card.className += ' color-option';
          card.style.backgroundColor = item.hex;
          const textColor = this.isLightColor(item.hex) ? '#333' : '#fff';
          card.innerHTML = `
            <div class="option-icon" style="font-size: 50px;">${item.emoji}</div>
          `;
          break;

        case 'animals':
          card.innerHTML = `
            <div class="option-icon">${item.emoji}</div>
            <div class="option-text">${item.name}</div>
          `;
          break;

        case 'vehicles':
          card.innerHTML = `
            <div class="option-icon">${item.emoji}</div>
            <div class="option-text">${item.name}</div>
          `;
          break;
      }

      // 点击事件
      card.addEventListener('click', () => this.selectAnswer(card, item));

      this.elements.optionsGrid.appendChild(card);
    });
  },

  /**
   * 选择答案
   */
  selectAnswer(card, selectedItem) {
    if (this.isAnswered) return;
    this.isAnswered = true;

    const { correct, category } = this.currentQuestion;
    const isCorrect = this.checkAnswer(selectedItem, correct, category);

    // 禁用所有选项
    document.querySelectorAll('.option-card').forEach(c => {
      c.classList.add('disabled');
    });

    if (isCorrect) {
      // 正确
      card.classList.add('correct');
      this.score += 10;
      this.updateScore();

      // 播放鼓励语
      SpeechModule.speakEncouragement();

      // 显示奖励
      setTimeout(() => {
        this.showReward();
      }, 800);
    } else {
      // 错误
      card.classList.add('wrong');

      // 播放再试一次
      SpeechModule.speakTryAgain();

      // 显示正确答案并允许重试
      setTimeout(() => {
        this.highlightCorrectAnswer();
        this.isAnswered = false;
        document.querySelectorAll('.option-card').forEach(c => {
          if (!c.classList.contains('correct')) {
            c.classList.remove('disabled');
          }
        });
        card.classList.add('disabled');
      }, 1000);
    }
  },

  /**
   * 检查答案是否正确
   */
  checkAnswer(selected, correct, category) {
    switch (category) {
      case 'letters':
        return selected.letter === correct.letter;
      case 'numbers':
        return selected.number === correct.number;
      case 'colors':
        return selected.name === correct.name;
      case 'animals':
        return selected.name === correct.name;
      case 'vehicles':
        return selected.name === correct.name;
      default:
        return false;
    }
  },

  /**
   * 高亮显示正确答案
   */
  highlightCorrectAnswer() {
    const { correct, category } = this.currentQuestion;
    const cards = document.querySelectorAll('.option-card');

    cards.forEach((card, index) => {
      const item = this.currentQuestion.options[index];
      if (this.checkAnswer(item, correct, category)) {
        card.classList.add('correct');
        card.classList.add('disabled');
      }
    });
  },

  /**
   * 播放当前题目声音
   */
  playCurrentSound() {
    if (!this.currentQuestion) return;

    const { correct, category } = this.currentQuestion;
    const btn = this.elements.playSoundBtn;

    // 添加播放动画
    btn.classList.add('playing');

    let text = '';
    switch (category) {
      case 'letters':
        text = correct.word;
        break;
      case 'numbers':
        text = correct.word;
        break;
      case 'colors':
        text = correct.name;
        break;
      case 'animals':
        text = correct.name;
        break;
      case 'vehicles':
        text = correct.name;
        break;
    }

    SpeechModule.speak(text).then(() => {
      btn.classList.remove('playing');
    });
  },

  /**
   * 更新分数显示
   */
  updateScore() {
    this.elements.scoreDisplay.textContent = this.score;
  },

  /**
   * 显示奖励弹窗
   */
  showReward() {
    const encouragements = [
      'Great Job! 🌟',
      'Amazing! ⭐',
      'Wonderful! 🎉',
      'Excellent! 🏆',
      'Super! 🌈'
    ];
    this.elements.rewardText.textContent =
      encouragements[Math.floor(Math.random() * encouragements.length)];
    this.elements.rewardPopup.classList.add('show');
  },

  /**
   * 隐藏奖励弹窗
   */
  hideReward() {
    this.elements.rewardPopup.classList.remove('show');
  },

  /**
   * 判断颜色深浅
   */
  isLightColor(hex) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness > 150;
  }
};

// 页面加载完成后初始化游戏
document.addEventListener('DOMContentLoaded', () => {
  QuizGame.init();
});
