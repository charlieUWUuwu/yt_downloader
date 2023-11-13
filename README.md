# yt_downloader

![screen](./img/screen.png)

## How to use
- Install the dependencies
```
$ git clone https://github.com/charlieUWUuwu/yt_downloader.git
$ conda install ffmpeg
$ pip install -r requirements.txt
```

- Quick start
```
python start.py
```

- Create an Executable using PyInstaller

  (You need to prepare your ico file, but it's optional)
```
pyinstaller -F -w --icon=MyICON.ico start.py
```

## TODO
直接使用pytube套件所下載的mp4，在上傳至手機時可能會出現錯誤，因此可參考mp3方式修改
