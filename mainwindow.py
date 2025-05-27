from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self. setWindowTitle("Custom Main Window")

        #Defining the menu bar
        menu_bar = self.menuBar()
        #creating a file menu
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit") #added quit within the file menu
        quit_action.triggered.connect(self.quit_app) #Added the ability to actualy quit

        #adding more to the menu bar
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy") #adding all these to the edit menu bar
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        setting_menu = menu_bar.addMenu("&Settings")
        help_menu = menu_bar.addMenu("&Help")

        #adding a toolbar!
        toolbar = QToolBar("The Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #added the ability ot quit via the toolbar
        toolbar.addAction(quit_action)

        #adding some other random action
        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        #adding another action with an image
        action2 = QAction(QIcon("action2.jpg"), "Some other action", self) #allows the image to be there instead of text
        action2.setStatusTip("Status message for the second action") #setting status messge for when you hover over it
        action2.triggered.connect(self.toolbar_button_click) #connects the button to the function
        action2.setCheckable(True) #toggles it within the toolbar (kind of shows if it is on or not)
        toolbar.addAction(action2) #just adding the action for whatever it does

        #adding a button wihtin the toolbar and the ability to separate them from others in the toolbar
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click me!!"))

        #adding a status bar
        self.setStatusBar(QStatusBar(self))

        #addding a button to make it even more fun!
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1)
        self.setCentralWidget(button1)

    def button1(self):
        print("button clicked!")

    def quit_app(self):
        self.app.quit() #defined the function to be able to quit

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from the app", 3000)

