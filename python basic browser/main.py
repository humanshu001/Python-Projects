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
        self.horizontal1 = QHBoxLayout()

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

        self.menu_bar = QToolButton()
        self.menu_bar.setText('☰')
        self.menu_bar.setMaximumHeight(30)
        self.menu_bar.setStyleSheet("background-color: #4CAF50; color: white;border-radius: 15px;font-weight:900;width: 30px; height: 30px; font-size: 15px;position:absolute")

        self.menu = QMenu()
        self.menu.addAction('New Tab').triggered.connect(self.new_tab)
        self.menu.addAction('New Window').triggered.connect(self.new_window)
        self.menu.addAction('History').triggered.connect(self.show_history)
        self.menu.addAction('Downloads').triggered.connect(self.show_downloads)
        self.menu.addAction('Bookmarks').triggered.connect(self.show_bookmarks)
        self.menu.addAction('Settings').triggered.connect(self.show_settings)
        self.menu.addAction('Exit').triggered.connect(self.exit_browser)
        self.menu.setStyleSheet("background-color: #333333; color: white;border-radius: 15px; font-size: 15px;")

        self.menu_bar.setMenu(self.menu)
        self.menu_bar.setPopupMode(QToolButton.InstantPopup)
        self.menu_bar.setArrowType(Qt.NoArrow)

        self.tab_view = QTabWidget()
        self.tab_view.setMaximumHeight(30)
        self.tab_view.setStyleSheet("border:none;background:#333333;color:black;font-size: 15px;width: 100%; height: 30px; position:absolute; top: 0px; left: 0px;")
        
        self.horizontal.setSpacing(0)
        
        self.horizontal1.addWidget(self.tab_view)


        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.horizontal.addWidget(self.menu_bar)
        self.browser = QWebEngineView()


        self.current_tab = QWidget()
        current_tab_layout = QVBoxLayout()
        current_tab_layout.addWidget(self.browser)
        self.current_tab.setLayout(current_tab_layout)
        self.tab_view.addTab(self.current_tab, "Current Tab")



        self.browser.audioMuted = False
        self.browser.page().profile().clearHttpCache()

        self.go_button.clicked.connect(lambda: self.Navigate(self.url_bar.text()))
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal1)
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl('http://www.google.com'))

        self.url_bar.setText(self.browser.url().toString())
        self.window.setLayout(self.layout)
        self.window.show()
        self.update_urlbar(self.browser.url())

        # set theme of website pages to dark
        self.browser.page().settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)

        # Connect the urlChanged signal to update_urlbar method
        self.browser.urlChanged.connect(self.update_urlbar)

        # search when click enter in url bar
        self.url_bar.returnPressed.connect(self.navigate_to_url)

    def Navigate(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    # function to update the url bar
    def update_urlbar(self, q):
        url = q.toString()
        self.url_bar.setText(url)
        self.url_bar.setCursorPosition(0)
        self.browser.setUrl(QUrl(url))

    # function to check if enter is pressed in the url bar
    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def new_tab(self):
        tab_widget = QWidget()
        tab_widget_layout = QVBoxLayout()
        web_browser = MyWebBrowser()
        tab_widget_layout.addWidget(web_browser.window)
        tab_widget.setLayout(tab_widget_layout)
        self.tab_view.addTab(tab_widget, "New Tab")


    def exit_browser(self):
        self.window.close()
    
    def show_settings(self):
        pass
    
    def show_bookmarks(self):
        pass

    def show_downloads(self):
        pass

    def show_history(self):
        pass

    def new_window(self):
        # run a new instance of the browser
        self.app = QApplication([])
        self.window = MyWebBrowser()
        self.app.exec_()

        


app = QApplication([])
window = MyWebBrowser()
app.exec_()
