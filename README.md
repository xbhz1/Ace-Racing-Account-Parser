# Ace-Racing-Account-Parser

本工具专用于批量查询和分析王牌竞速游戏中的其他玩家账号信息，以判断其是否为“小号炸鱼”行为。请确保他人炸鱼账号与大号为同一个游戏账号，否则会无法查询，因为不支持跨账户操作

### 功能特性：
- [✔] 支持批量处理
- [✔] 支持内容导出
- [✘] 不支持跨账户操作

脚本目前仅在termux做测试，其他平台请自行安装必要库并修改逻辑
1. **安装Python**
```bash
pkg install python
```
2. **安装requests库**
```bash
pip install requests
```
### 使用指南：

1. **运行脚本 1**
   ```bash
   python race.py
   ```

  在命令行中输入您自行获取的玩家ID（例如：`1179370108100764`）。
   
   _执行后，数据将保存到以下文件:
   plaintext
   data/测试玩家..json
   
2. **运行脚本 2**
   ```bash
   python plcl.py
   ```

3. **运行脚本 3**
   ```bash
   python lb.py
   ```
   接着请输入包含相关数据的文件夹路径：
   
   ```bash
   /Ace Racing/Account Parser/python/lb.txt
   ```
   执行后，新的或更新的数据同样会保存至指定的数据文件。

**注意：**
- 玩家ID可通过游戏回放文件或其他合法途径获取。
- 游戏回放文件路径files/LocalData/ReplayData/646643646464644646464/history_replay/
