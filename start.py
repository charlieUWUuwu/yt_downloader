# ref : https://www.wongwonggoods.com/all-posts/python/pyqt5/pyqt5-1/

'''
注意 : .ui 更改後請重新執行指令 pyuic5 -x test.ui -o UI.py 以重新生成.py
說明 :
    -x: 輸出為可單獨執行的檔案 (有 main 的部分)，若無會只有單純封裝好的 UI class
    -o: 輸出 .py 檔案
'''

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from controller import myMainWindow_controller
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = myMainWindow_controller()

    # 設置視窗大小
    window.setFixedSize(533, 399)
    # 設置視窗名稱
    window.setWindowTitle("Charlie's youtube downloader")
    # 設置視窗 icon
    icon = QIcon("charlie.ico")
    window.setWindowIcon(icon)

    window.show()
    sys.exit(app.exec_())