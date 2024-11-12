# controller 部分
from PyQt5 import QtWidgets
from pytubefix import YouTube
from PyQt5.QtCore import QCoreApplication
import os, MyUI

from pydub import AudioSegment # 錯誤mp3 轉換到 正常mp3 (初步研判為編碼問題...)


class myMainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MyUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_control() # 元件初始化

    def setup_control(self): # 元件初始化
        self.ui.plainTextEdit.setPlaceholderText('https://') # 設置提示文字
        self.ui.fileButton.clicked.connect(self.buttonChooseFile)
        self.ui.pushButton_2.clicked.connect(self.button_mp3) # mp3下載確認按鈕
        self.ui.pushButton.clicked.connect(self.button_mp4)  # mp4下載確認按鈕
        self.ui.clearButton.clicked.connect(self.buttonClear) # 取消按鈕
        self.ui.progressBar.setValue(0) # 進度條重置
        self.ui.showMsg.clear()
        self.ui.showDone.clear()
        self.ui.label.setText("選擇位置") 

    def buttonClear(self):
        self.ui.label.setText("選擇位置") 
        self.ui.progressBar.setValue(0) 
        self.ui.plainTextEdit.clear()
        self.ui.showMsg.clear()
        self.ui.showDone.clear()

    def buttonChooseFile(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None,"選取資料夾","C:/")  # 起始路徑
        if directory == "":
            directory = "選擇位置"
        self.ui.label.setText(str(directory)) 
        self.ui.showMsg.clear()

    def progress_callback(self, stream, chunk, bytes_remaining):
        # 計算下載進度百分比
        total_size = stream.filesize # 取得完整尺寸
        bytes_downloaded = total_size - bytes_remaining  # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
        progress = int(bytes_downloaded / total_size * 100)

        # 更新進度條
        self.ui.progressBar.setValue(progress)

    def button_mp4(self):
        self.ui.progressBar.setValue(0)  # 重置進度
        self.ui.showDone.clear()
        self.ui.showMsg.clear()
        url = self.ui.plainTextEdit.toPlainText() # 取得網址
        destination = self.ui.label.text()

        QCoreApplication.processEvents()
        
        try:
            if destination != "選擇位置" and url != "" :
                # progress_callback 用於設置進度條
                yt = YouTube(url, on_progress_callback=self.progress_callback)
                video_name = str(yt.title).replace(":", " ")
                video_name = video_name.replace("/", " ")

                # 檢查是否有相同檔名的文件存在，否則會錯誤
                if os.path.exists(destination+'/'+str(video_name)+'.mp4'):
                    self.ui.showMsg.setText('這個影片好像下載過了喔，名稱是:' + str(video_name) + '.mp4')
                    self.ui.showDone.setText("下載過了:0")
                else:
                    video = yt.streams.get_highest_resolution()
                    video.download(output_path=destination, filename=video_name + '.mp4') # 如果沒有設定 filename，則以原本影片的 title 作為檔名

                    self.ui.showMsg.setText(str(video_name)+str(".mp4"))
                    self.ui.showDone.setText("下載完成:)")
            else:
                self.ui.showDone.setText("下載失敗:(")
                self.ui.showMsg.setText('請確定影片網址與資料夾都有設定好喔~')
        except:
            self.ui.showMsg.setText('網址錯誤或影片可能有年齡限制，請換一個呦。')

    # https://hackmd.io/@XAPAE2ZvTu-ppTbSPNtsFQ/SJL4QqQ7b?type=view
    def trans_mp3_to_mp3(self, filepath):
        with open(filepath,'rb') as f:
          song = AudioSegment.from_file(filepath)
          song.export(filepath, format='mp3', parameters=['-loglevel', 'quiet'])

    def button_mp3(self):
        self.ui.progressBar.setValue(0)  # 重置進度
        self.ui.showDone.clear()
        self.ui.showMsg.clear()
        url = self.ui.plainTextEdit.toPlainText() # 取得網址
        destination = self.ui.label.text()

        QCoreApplication.processEvents()
        
        try:
            if destination != "選擇位置" and url != "" :
                # progress_callback 用於設置進度條
                yt = YouTube(url, on_progress_callback=self.progress_callback)
                song_name = str(yt.title).replace(":", " ")
                song_name = song_name.replace("/", " ")

                # 檢查是否有相同檔名的文件存在，否則會錯誤
                if os.path.exists(destination+'/'+str(song_name)+'.mp3'):
                    self.ui.showMsg.setText('這個影片好像下載過了喔，名稱是:' + str(song_name) + '.mp3')
                    self.ui.showDone.setText("下載過了:0")
                else:
                    song_path = yt.streams.get_audio_only().download(mp3=True, output_path=destination)
                    self.trans_mp3_to_mp3(song_path) # 轉為符合格式的 mp3
                    self.ui.showMsg.setText(song_name+str(".mp3"))
                    self.ui.showDone.setText("下載完成:)")
            else:
                self.ui.showDone.setText("下載失敗:(")
                self.ui.showMsg.setText('請確定影片網址與資料夾都有設定好喔~')
        except:
            self.ui.showMsg.setText('網址錯誤或影片可能有年齡限制，請換一個呦。')