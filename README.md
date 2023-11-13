# yt_downloader

## How to use
- 安裝相關套件
```
conda install ffmpeg
pip install -r requirements.txt
```

- 快速執行
```
python start.py
```

- 打包成exe(需自行準備 ico ，或不設定)
```
pyinstaller -F -w --icon=MyICON.ico start.py
```

## 未來待辦改進
直接使用pytube套件所下載的mp4，在上傳至手機時可能會出現錯誤，因此可參考mp3方式修改
