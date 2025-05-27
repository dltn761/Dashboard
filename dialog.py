import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("The Form")

if __name__ == "__main__":
    #creates the application
    app = QApplication(sys.argv)
    #creates and shows the form
    form = Form()
    form.show()
    #runs the main Qt Loop
    sys.exit(app.exit())