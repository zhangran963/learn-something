tesseract: 是一款开源的图像识别库;
* 安装: `brew install tesseract`;
* 下载合适语言包: `https://github.com/tesseract-ocr/tessdata`;
* 本地语言包地址`/usr/local/Cellar/tesseract/3.05.02/share/tessdata`;
* 查看支持的语言`tesseract --list-langs`;
* 开始识别: `tesseract 图片名称 保存文件名称 -l 语言1+语言2...`;



### python中应用 tesseract
```py
pip install pytesseract
```