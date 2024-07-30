# biquge-spider
### 笔趣阁 小说爬取

目录结构

```shell
# 笔趣阁
├─ Novel                   # 下载的小说目录
│    └─ 修罗武神           # 小说目录
├─ README.md				
├─ __pycache__
├─ img						
│    └─ bug.ico
├─ lib                    # 模块目录
│    ├─ IP.py             # IP 代理池
├─ main.py                # 主文件 运行文件
├─ src
│    ├─ Spider.py         # 爬虫代码文件
```



依赖模块：

- requests
- lxml
- 其他模块 python 3.11.0 内置了





安装模块以及启动程序：

```shell

pip install requests

pip install lxml

python main.py

```



启动程序后需要输入两个地址

第一个地址输入笔趣阁最新的网址，例如：https://www.bqgbi.com

第二个地址输入要下载小说的地址，例如：https://www.bqgbi.com/book/876/



如果电脑没有 python 环境的话，我也有打包好的 exe 文件可以直接运行 https://github.com/Shimiankang/biquge-spider/releases/tag/v1.0.0
