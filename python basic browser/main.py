from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser():

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle('My Browser')

        self.window.setStyleSheet("background-color: #333333; color: #ffffff;")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setStyleSheet("background-color: #444444; color: white;border-radius: 5px;height: 30px; font-size: 15px;")

        self.go_button = QPushButton('🔍')
        self.go_button.setMaximumHeight(30)
        self.go_button.setStyleSheet("background-color: #4CAF50; color: white;border-radius: 15px;width:30px; height: 30px; font-size: 15px;")

        self.back_button = QPushButton('🡸')
        self.back_button.setMaximumHeight(30)
        self.back_button.setStyleSheet("background-color: #4CAF50; color: white;border-radius: 15px;font-weight:900;width: 30px; height: 30px; font-size: 15px")

        self.forward_button = QPushButton('🢂')
        self.forward_button.setMaximumHeight(30)
        self.forward_button.setStyleSheet("background-color: #4CAF50; color: white;border-radius: 15px;font-weight:900;width: 30px; height: 30px; font-size: 15px")

        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.browser = QWebEngineView()

        self.browser.audioMuted = False
        self.browser.page().profile().clearHttpCache()

        self.go_button.clicked.connect(lambda: self.Navigate(self.url_bar.text()))
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl('http://www.google.com'))

        self.window.setLayout(self.layout)
        self.window.show()

    def Navigate(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
app.exec_()
