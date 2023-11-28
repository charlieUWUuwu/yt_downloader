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
  
  - step1 : copy the folder 'path/to/ffmpeg' into the current folder

  - step2 : 
  ```
  pyinstaller -F -w --add-binary "./ffmpeg/Library/bin;." --icon=MyICON.ico start.py
  ```
