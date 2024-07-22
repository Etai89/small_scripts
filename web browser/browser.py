# Importing required PyQt5 modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

# Create the main class for the web browser
class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Initialize the parent class with the given arguments
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        # Set the window title for the browser
        self.setWindowTitle("Etai Web Browser")

        # Create a vertical layout for the main window
        self.layout = QVBoxLayout()
        # Create a horizontal layout for the URL bar and navigation buttons
        self.horizontal = QHBoxLayout()

        # Create a line edit widget for the URL bar
        self.url_bar = QLineEdit()
        # Set the maximum height for the URL bar to 30
        self.url_bar.setMaximumHeight(30)

        # Create a button widget for the "GO" button
        self.go_btn = QPushButton("GO")
        # Set the minimum height for the "GO" button to 30
        self.go_btn.setMinimumHeight(30)

        # Create a button widget for the "Back" button
        self.back_btn = QPushButton("<=")
        # Set the minimum height for the "Back" button to 30
        self.back_btn.setMinimumHeight(30)

        # Create a button widget for the "Forward" button
        self.forward_btn = QPushButton("=>")
        # Set the minimum height for the "Forward" button to 30
        self.forward_btn.setMinimumHeight(30)

        # Add the URL bar and navigation buttons to the horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        # Create a web engine view widget for the browser
        self.browser = QWebEngineView()

        # Connect the "GO" button to the `navigate` function and pass the text in the URL bar as the argument
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        # Connect the "Back" button to the `back` function of the browser widget
        self.back_btn.clicked.connect(self.browser.back)
        # Connect the "Forward" button to the `forward` function of the browser widget
        self.forward_btn.clicked.connect(self.browser.forward)

        # Add the horizontal layout and browser widget to the vertical layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # Create a central widget and set the vertical layout as its layout
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        # Set the central widget as the central widget of the main window
        self.setCentralWidget(central_widget)

        # Set the initial URL to load in the browser window
        # "http://duckduckgo.com" is the default URL set in the browser
        self.browser.setUrl(QUrl("http://duckduckgo.com"))
        # Show the browser window
        self.show()

    def navigate(self, url):
        # Check if the URL entered does not start with "http"
        if not url.startswith("http"):
            # In that case, add "http://" before the URL
            url = "http://" + url
            # Update the URL in the URL bar with the complete URL
            self.url_bar.setText(url)
            # Load the URL in the browser window
        self.browser.setUrl(QUrl(url))

# Create an instance of the QApplication class
app = QApplication([])
# Create an instance of the MyWebBrowser class
window = MyWebBrowser()
# Run the application
app.exec_()
