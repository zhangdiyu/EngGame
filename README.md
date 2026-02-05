# ABC Learning - 幼儿英语学习游戏

专为3岁幼儿设计的网页英语启蒙游戏，通过视觉和听觉互动帮助孩子学习英语字母、数字、颜色和动物。

## 功能模块

- **字母学习 (ABC)**: 26个英文字母，配合代表单词和图标
- **数字学习 (123)**: 数字1-10，配合数量圆点展示
- **颜色学习 (Colors)**: 8种基础颜色
- **动物学习 (Animals)**: 12种常见动物
- **测验游戏 (Quiz)**: 听音选图的互动游戏

## 技术特点

- 纯前端实现，无需后端服务
- 使用 Web Speech API 实现英语发音
- 响应式设计，完美适配 iPad
- 触摸优化，超大点击区域

## 部署到 Mac Mini

### 方式一：使用 Python（推荐）

macOS 自带 Python，无需安装任何软件。

```bash
# 1. 将项目文件夹复制到 Mac Mini
# 2. 打开终端，进入项目目录
cd /path/to/EngGame

# 3. 启动 HTTP 服务器
python3 -m http.server 8080
```

服务器启动后会显示：
```
Serving HTTP on :: port 8080 (http://[::]:8080/) ...
```

### 方式二：使用 Node.js

如果已安装 Node.js：

```bash
# 安装 http-server（只需一次）
npm install -g http-server

# 启动服务器
cd /path/to/EngGame
http-server -p 8080
```

## 在 iPad 上访问

1. 确保 iPad 和 Mac Mini 在同一个 WiFi 网络
2. 在 Mac Mini 上查看 IP 地址：
   - 系统偏好设置 → 网络 → 查看 IP 地址
   - 或终端执行：`ifconfig | grep "inet "`
3. 在 iPad Safari 中访问：`http://[Mac-IP]:8080`
   - 例如：`http://192.168.1.100:8080`

## 添加到 iPad 主屏幕

为获得更好的全屏体验：

1. 在 Safari 中打开游戏页面
2. 点击分享按钮 (方框+箭头)
3. 选择"添加到主屏幕"
4. 输入名称后点击"添加"

## 开机自动启动服务器

创建启动脚本，让 Mac Mini 开机后自动运行服务器：

1. 创建启动脚本 `~/start-game-server.sh`：
```bash
#!/bin/bash
cd /path/to/EngGame
python3 -m http.server 8080
```

2. 添加执行权限：
```bash
chmod +x ~/start-game-server.sh
```

3. 添加到登录项：
   - 系统偏好设置 → 用户与群组 → 登录项
   - 添加此脚本

## 浏览器兼容性

- ✅ iPad Safari (推荐)
- ✅ Chrome
- ✅ Firefox
- ✅ Edge

## 注意事项

- iOS Safari 需要用户首次点击屏幕后才能播放声音（浏览器安全限制）
- 建议将 iPad 音量调至适中
- 首次加载可能需要等待图标库加载

## 自定义内容

如需修改学习内容，编辑 `js/data.js` 文件：

- `letters`: 字母及代表单词
- `numbers`: 数字1-10
- `colors`: 颜色列表
- `animals`: 动物列表

图标来自 [Font Awesome](https://fontawesome.com/icons)，可在官网搜索更多图标。
