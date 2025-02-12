### 项目介绍
一个附属于[BetterGI](https://github.com/babalae/better-genshin-impact)的项目，通过bettergi的webhook构建。<br>
当BetterGI使用webhook发送通知的时候，运行本项目可以接受其数据然后存储在本地的Sqlite数据库中，用户可以访问本地http://127.0.0.1:222 来查阅BetterGI发送的通知。使用python的flask构建服务器后端。<br>
当前bettergi的版本号：0.41.0<br>
主要运用在BetterGI一条龙模块，下文有使用说明。<br>
项目截图（测试图）<br>
<img src="https://github.com/user-attachments/assets/ea9d14b3-61a8-4fdc-a9c8-edf111b63d83" alt="示例图片" width="394" height="501">

### 使用方法（自行配置python环境）
1. 克隆本项目到本地
2. 点击运行`run run.py.bat`启动服务器。出现`服务已启动...`无报错则启动成功。在浏览器输入`http://127.0.0.1:222`即可查阅。首次启动无信息。
3. 配置bettergi的webhook信息。左下角的`设置`点击进入，然后webhook端点如图设置即可。当服务器启动后可以点击`发送`按钮检查是否可行。
<img src="https://github.com/user-attachments/assets/317470d0-94cb-4a93-af3b-c3896e59bfe3" alt="示例图片">

4. （可选）使用内网穿透，注意转发本地端口222。 [这是找的B站视频，非本人录制](https://www.bilibili.com/video/BV1KF411m7Z7) 。之后可以在非局域网内访问网页端口。这里可能存在国内网站备案问题，请注意遵守相关法律。

### 继续开发

你可以使用`test.py`来记录webhook发送的POST数据包（无网页前端）<br>
[webhook文档](https://bettergi.com/dev/webhook.html)<br>
**文件说明**<br>
`init_database.py`：初始化数据库，构建对应的数据模型，如果有test.py生成的txt文件则会导入到数据库中。<br>
`main.py`：主要的服务器程序。<br>
`run.py`：以WSGI服务器运行`main.py`<br>
`test.py`：只接受来自BetterGI的POST数据，然后以json的格式保存在post_load/###.txt 文件中。格式为：<br>
<img src="https://github.com/user-attachments/assets/13570b41-8da5-4c4e-8c4e-14355c5d75ac" alt="示例图片" height="368" width="362">

---

### 法律免责声明

本开源项目由Because66666开发并提供。在使用本项目之前，请仔细阅读以下免责声明：<br>
一、项目性质与使用风险<br>
本开源项目是基于python而开发的，旨在为开发者社区提供一种BetterGI的webhook可视化的解决方案。然而，由于开源项目的复杂性和开发环境的多样性，本项目可能存在各种潜在的技术缺陷、漏洞或其他问题。开发者在使用本项目时，应充分认识到这些潜在风险，并自行承担由此可能产生的一切后果。<br>
二、责任限制<br>
技术风险：开发者不保证本项目的性能、稳定性、安全性或兼容性。在任何情况下，开发者不对因使用本项目而导致的任何直接、间接、偶然、特殊或后果性的损害承担责任，包括但不限于数据丢失、系统故障、业务中断或利润损失等。<br>
知识产权风险：尽管开发者已尽合理努力确保本项目不侵犯任何第三方的知识产权，但开发者不能保证本项目完全不存在知识产权争议。如果因使用本项目而引发任何知识产权纠纷，开发者不承担任何责任，用户应自行解决相关争议并承担相应费用。<br>
法律合规风险：开发者不保证本项目符合所有国家和地区的法律法规要求。用户在使用本项目时，应确保其使用行为符合当地法律法规的规定。如果因用户违反法律法规而产生任何法律后果，开发者不承担任何责任。<br>
三、项目更新与维护<br>
开发者可能会根据自身计划和资源情况对本项目进行更新和维护。然而，开发者不保证项目更新的及时性、频率或质量。用户应自行关注项目更新信息，并在使用前确保所使用的版本符合其需求。如果用户因未及时更新项目而导致任何问题，开发者不承担任何责任。<br>
四、用户反馈与支持<br>
开发者欢迎用户对本项目提出反馈和建议，但开发者不保证对所有反馈和建议进行回复或采纳。此外，开发者不提供任何形式的商业支持或保证。用户在使用过程中遇到问题时，应自行寻求解决方案或通过社区渠道获取帮助。<br>
五、免责声明的适用范围<br>
本免责声明适用于本开源项目的全部内容，包括但不限于源代码、文档、示例代码、工具等。用户在下载、安装、使用或分发本项目时，即视为已充分理解并同意接受本免责声明的全部条款。<br>
开发者希望用户能够理解并接受上述免责声明，合理、谨慎地使用本开源项目。开发者将尽最大努力确保项目的质量和发展，但无法承担因使用本项目而产生的一切潜在法律后果。如果您对本免责声明有任何疑问或需要进一步的信息，请通过Github[开源地址](https://github.com/Because66666/better_gi_miniweb)的Issues与开发者联系。<br>
Because66666<br>
2025.1.21<br>
