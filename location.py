import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from maps import map

def locshow():
    map()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.load(QUrl("C:/Users/dr_de/OneDrive/Documents/VS/map.html"))
    web.show()
    app.exec_()
